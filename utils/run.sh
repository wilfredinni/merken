python manage.py collectstatic --noinput
python manage.py migrate
gunicorn conf.wsgi.prod --bind=0.0.0.0:80
