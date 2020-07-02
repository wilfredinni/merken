python manage.py collectstatic --noinput --settings=conf.settings.prod
python manage.py migrate --settings=conf.settings.prod
gunicorn conf.wsgi --bind=0.0.0.0:80
