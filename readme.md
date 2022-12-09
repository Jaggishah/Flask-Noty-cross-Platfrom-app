For Creating db

from project import app, db
app.app_context().push()
db.create_all()

pip freeze > requirements.txt

echo web: gunicorn app:app > Procfile