from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import glob
import pandas as pd
import time
from home.models import WeatherData

class Command(BaseCommand):
    help = 'Extracting data from weather data file'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        start = time.time()
        self.stdout.write(" Extracting weather data from given path")
        path = f"{str(settings.BASE_DIR)}/wx_data/*.txt"
        list_files = glob.glob(path)
        wx_header = ['date', 'temp_high', 'temp_low', 'precip']
        self.stdout.write(f"Weather directory contain : {len(list_files)}")
        main_df = pd.DataFrame()
        self.stdout.write("Preparing weather data into dataframe before pushing to database")
        for weather_station_file in list_files:
            work_station = weather_station_file.split('/')[-1].split('.')[0]
            self.stdout.write(f"Processing {work_station}")
            df = pd.read_csv(weather_station_file, delim_whitespace=True, header=None, names=wx_header)

            df['station'] = work_station
            df['date'] = pd.to_datetime(df['date'].astype(str))
            df['year'] = df['date'].dt.year
            df.drop_duplicates(subset=['date', 'temp_high', 'temp_low', 'precip'], keep=False, inplace=True)
            main_df = pd.concat([main_df, df], ignore_index=True)
        data_extraction_done = time.time()
        data_extraction = data_extraction_done - start
        self.stdout.write("Preparation has been completed, pushing to database")
        self.stdout.write(f"Total record count: {main_df.shape[0]}")
        self.stdout.write(f"Total data preparation time: {data_extraction}")

        main_df['temp_high'] = main_df['temp_high'].apply(lambda x: float(x/10.0) if x != '-9999' else x)
        main_df['temp_low'] = main_df['temp_low'].apply(lambda x: float(x/10.0) if x != '-9999' else x)
        main_df['precip'] = main_df['precip'].apply(lambda x: float(x/10.0) if x != '-9999' else x)

        bulk_objects_lists = [
            WeatherData(
                date = bulk_item['date'],
                weather_station = bulk_item['station'],
                temp_high = bulk_item['temp_high'],
                temp_low =bulk_item['temp_low'],
                precip = bulk_item['precip'],
                year = bulk_item['year'],
            )
            for idx, bulk_item in main_df.iterrows()]

        WeatherData.objects.bulk_create(bulk_objects_lists, ignore_conflicts= True)
        self.stdout.write("Successfully saved the weather data into database")
        done = time.time()
        total_elapsed = done - start
        self.stdout.write(f"Total elapsed time: {total_elapsed}")


