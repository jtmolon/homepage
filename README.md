# homepage

Homepage project for personal (or anything else) webpage including blog. Powered by [https://wagtail.io/](wagtail)

## Installation

- Create a virtualenv, activate it and install the requirements
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install requirements.txt
```

- Run Django migrations, create a superuser and startup the application
```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

- Application will be available at [http://127.0.0.1:8000]
