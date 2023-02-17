## WEATHER ANALYSIS

This project contains the real time implementation of the weather analysis 
of existing dataset provided from the [source data](https://github.com/corteva/code-challenge-template/blob/main/wx_data/)

The project is developed with following technical skillsets

| No  |  Skill |  Description |
| ------------ | ------------ | ------------ |
|  1 | Python  |  Programming Language |
|  2 |  Django |  Frame work |
|  3 |  Django RestFramework |  To Develop Rest API's |
|  4 |  Sqlite3 |   Database|
| 5  |  Swagger |   API documentation|



## Installation

#### Clone directory
```
daemon-2 ripend_pro % git clone https://github.com/Patel061274/weather.git 

Cloning into 'weather'...
remote: Enumerating objects: 208, done.
remote: Counting objects: 100% (208/208), done.
remote: Compressing objects: 100% (205/205), done.
remote: Total 208 (delta 1), reused 208 (delta 1), pack-reused 0
Receiving objects: 100% (208/208), 11.57 MiB | 9.70 MiB/s, done.
Resolving deltas: 100% (1/1), done.
daemon-2 ripend_pro % 
```
#### Export Project 

```
daemon-2 ripend_pro % cd weather
daemon-2 weather % tree
.
├── Readme.md
├── home
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── management
│   │   ├── __init__.py
│   │   └── commands
│   │       ├── __init__.py
│   │       ├── extract_data.py
│   │       └── generate_weather_stats.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── pagination.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── weather
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── wx_data
    ├── USC00110072.txt
    ├── USC00110187.txt
    ├── USC00110338.txt
    ├── USC00111280.txt
    .........
    .........
```

### Install Requirements

```
daemon-2 weather % virtualenv .weather_env
daemon-2 weather % source ./.weather_env/bin/activate
(.weather_env)daemon-2 weather %
(.weather_env) daemon-2 weather % pip install -r requirements.txt
(.weather_env) renjithsraj@daemon-2 weather % pip freeze
appnope==0.1.3
asgiref==3.6.0
asttokens==2.2.1
backcall==0.2.0
certifi==2022.12.7
charset-normalizer==3.0.1
coreapi==2.3.3
coreschema==0.0.4
decorator==5.1.1
Django==4.1.6
django-rest-fr ..
....
```

### DB Configuration

```
(.weather_env) daemon-2 weather % python manage.py makemigrations home
No changes detected in app 'home'

(.weather_env) daemon-2 weather % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, home, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying home.0001_initial... OK
  Applying sessions.0001_initial... OK
```

### Extract Data

`extract_data` is a management command to extract and load the data into the table. 

```
(.weather_env) renjithsraj@daemon-2 weather % python manage.py extract_data

 Extracting weather data from given path
Weather directory contain : 167
Preparing weather data into dataframe before pushing to database
Processing USC00257715
Processing USC00113879
Processing USC00127935
........
.....
...
.
Processing USC00259090
Preparation has been completed, pushing to database
Total record count: 1729957
Total data preparation time: 3.1130619049072266
Successfully saved the weather data into database
Total elapsed time: 67.87534189224243
```

### Generate Weather Stts analysis data

`generate_weather_stats` is management command to generate the analysis data from weather data loaded in last step.

(.weather_env) daemon-2 weather % python manage.py generate_weather_stats
Extracting data from WeatherData to Process data analysis
Total WeatherData count: 4820
Successfully inserted analysed data into WeatherDataStats
```

### Run Application

#### Create Super User

```
(.weather_env) daemon-2 weather % python manage.py createsuperuser
Username (leave blank to use 'admin'): admin
Email address: 
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

Run Application

```
(.weather_env) daemon-2 weather % python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 17, 2023 - 17:19:06
Django version 4.1.6, using settings 'weather.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### API's

- http://127.0.0.1:8000/api/weather
- http://127.0.0.1:8000/api/weather/stats

### Swagger API documentation [http://127.0.0.1:8000/doc/]

- [ Swagger document](http://127.0.0.1:8000/doc/)

### Screen Shots

- Swagger Document 1

![Swagger Document](https://github.com/Patel061274/weather/blob/main/pics/Screenshot%202023-02-17%20at%208.27.39%20PM.png)


- Weather Data API

![Weather Data API](https://github.com/Patel061274/weather/blob/main/pics/Screenshot%202023-02-17%20at%208.28.21%20PM.png)

- Weather Data Stats API

![Weather Data Stats API](https://github.com/Patel061274/weather/blob/main/pics/Screenshot%202023-02-17%20at%208.28.21%20PM.png)











