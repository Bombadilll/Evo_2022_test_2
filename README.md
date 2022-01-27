# Evo_2022_test_2


Simple  website for test on Evo2022.

Users can create an account with a username and password,say welcome, and see all visitors and date of visit/ 


## Installing

### Requirements

* [Python](https://python.org) 3.9.10 
* [PostgreSQL](https://www.postgresql.org) running with a _database_, _username_ and _password_ to be used with Pets.
Don't forget fix  settings.py for Django.

### Fork and clone the repository

First fork the project using GitHub, than clone it locally:

```console
https://github.com/Bombadilll/Evo_2022_test_2.git

```


#### Basic Django settings

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


#### Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your DB',
        'USER': 'your superuser',
        'PASSWORD': 'your pass',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}




### Other dependencies

gunicorn==20.1.0
django==4.0.1
psycopg2==2.9.3
dj-database-url==0.5.0
whitenoise==5.3.0

### Heroku deploy
See worked site on  Heroku
https://evo2022test2.herokuapp.com/




