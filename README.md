# KodLand Interview Task

## Installation

- Create venv and install dependencies

```
$ python3 -m venv .venv
$ source ./.venv/bin/activate
$ pip install -r requirements.txt
```

- Create database

```
$ sudo -u postgres psql
postgres=# CREATE DATABASE kodland_blog;
postgres=# CREATE USER kodland WITH PASSWORD 'qwerty12+';
postgres=# ALTER ROLE kodland SET client_encoding TO 'utf8';
postgres=# ALTER ROLE kodland SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE kodland SET timezone TO 'UTC';
postgres=# GRANT ALL PRIVILEGES ON DATABASE kodland_blog TO kodland;
postgres=# \q
```

- Configure database in django project settings (`./app/app/settings.py`)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kodland_blog',
        'USER': 'kodland',
        'PASSWORD': 'qwerty12+',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- Apply migrations and create superuser (if you would inspect `/admin`)

```
$ python app/manage.py migrate
$ python app/manage.py createsuperuser
```

- Run server and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

```
$ python app/manage.py runserver
```
