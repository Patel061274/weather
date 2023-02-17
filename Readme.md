## WEATHER ANALYSIS

This project contains the real time implementation of the weather analysis 
of existing dataset provided from the [source data](https://github.com/corteva/code-challenge-template/blob/main/wx_data/)

### Problem Statement.


This coding exercise will help us understand how you approach some of the common problems we see in data engineering. Ask questions if things are unclear, use best practices and common software patterns, and feel free to go the extra mile to show off your skills. Imagine you are handing off your completed project to someone else to maintain -- it should be clear to another developer how things work and your reasoning behind your design decisions.

You will be asked to ingest some weather and crop yield data (provided), design a database schema for it, and expose the data through a REST API. You may use whatever software tools you would like to answer the problems below, but keep in mind the skills required for the position you are applying for and how best to demonstrate them. Read through all the problems before beginning, as later problems may inform your approach to earlier problems.

You can retrieve the data required for this exercise by cloning this repository:
https://github.com/corteva/code-challenge-template

Weather Data Description
------------------------

The wx_data directory has files containing weather data records from 1985-01-01 to 2014-12-31. Each file corresponds to a particular weather station from Nebraska, Iowa, Illinois, Indiana, or Ohio.

Each line in the file contains 4 records separated by tabs: 

1. The date (YYYYMMDD format)
2. The maximum temperature for that day (in tenths of a degree Celsius)
3. The minimum temperature for that day (in tenths of a degree Celsius)
4. The amount of precipitation for that day (in tenths of a millimeter)

Missing values are indicated by the value -9999.

Problem 1 - Data Modeling
-------------------------
Choose a database to use for this coding exercise (SQLite, Postgres, etc.). Design a data model to represent the weather data records. If you use an ORM, your answer should be in the form of that ORM's data definition format. If you use pure SQL, your answer should be in the form of DDL statements.

Problem 2 - Ingestion
---------------------
Write code to ingest the weather data from the raw text files supplied into your database, using the model you designed. Check for duplicates: if your code is run twice, you should not end up with multiple rows with the same data in your database. Your code should also produce log output indicating start and end times and number of records ingested.

Problem 3 - Data Analysis
-------------------------
For every year, for every weather station, calculate:

* Average maximum temperature (in degrees Celsius)
* Average minimum temperature (in degrees Celsius)
* Total accumulated precipitation (in centimeters)

Ignore missing data when calculating these statistics.

Design a new data model to store the results. Use NULL for statistics that cannot be calculated.

Your answer should include the new model definition as well as the code used to calculate the new values and store them in the database.

Problem 4 - REST API
--------------------
Choose a web framework (e.g. Flask, Django REST Framework). Create a REST API with the following GET endpoints:

/api/weather
/api/weather/stats

Both endpoints should return a JSON-formatted response with a representation of the ingested/calculated data in your database. Allow clients to filter the response by date and station ID (where present) using the query string. Data should be paginated.

Include a Swagger/OpenAPI endpoint that provides automatic documentation of your API.

Your answer should include all files necessary to run your API locally, along with any unit tests.


------------

###  How to install

Clone the directory into the local directory using `git clone <repo name>`

``````shell
daemon-2  %  git clone <repo name>
daemon-2  %  cd weather
daemon-2 weather %  virtualenv .weather_ase
daemon-2 weather % source ./.weather_ase/bin/activate
(.weather_ase) renjithsraj@daemon-2 weather % pip install -r requirements.txt
```

### Pre Run Activities

```shell
(.weather_ase) daemon-2 weather % python manage.py makemigrations home
(.weather_ase) daemon-2 weather % python manage.py migrate

```

### Load Data

To load the data into the table use below management command., this command will load the data into the table using pandas and bulk create using django ORM. 

Ingest the weather data from the raw text files supplied into your database, using the model you designed. Check for duplicates: if your code is run twice, you should not end up with multiple rows with the same data in your database. Your code should also produce log output indicating start and end times and number of records ingested.


```shell
(weather_ase) daemon-2 weather % python manage.py extract_data
```

### Generate Analytical Data

To load the analytical data into the db using below management command. This command will loaded the data for below points.

For every year, for every weather station, calculate:

* Average maximum temperature (in degrees Celsius)
* Average minimum temperature (in degrees Celsius)
* Total accumulated precipitation (in centimeters)

```shell
(.weather_ase) daemon-2 weather % python manage.py generate_weather_stats
```

### How to Run
```shell
(.weather_ase) daemon-2 weather % python manage.py runserver
```

### API TESTING






