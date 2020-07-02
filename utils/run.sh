python manage.py collectstatic --noinput
python manage.py migrate
gunicorn conf.wsgi --bind=0.0.0.0:80
