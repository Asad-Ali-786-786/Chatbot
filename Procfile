web: gunicorn chatbot_project.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn chatbot_project.wsgi

python -m dotenv set > /app/.env && python manage.py runserver 0.0.0.0:$PORT

