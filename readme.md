## API SILVERTEC INFORMÁTICA

<p>api building for use in site Silvertec Informática</p>

* python 3.6+
* django 2.0+
* django-rest-framework 3+

### Configurations

* Create and activate env
```sh
python -m venv venv
souce venv/bin/activate
```
* install dependencies

```sh
pip install -r requirements.txt
```
* run migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

* create superuser

```sh
python manage.py createsuperuser
```

* run tets

```sh
python manage.py test
```