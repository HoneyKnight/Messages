# Messages


### Проект "**Messages**" был создан для автоматизации работы отдела. К определенным городам привязаны шаблоны сообщений для записи кандидатов на собеседования.

### Локальный запуск:
```python
py -3.7 -m venv venv
source venv/scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
cd messages
```python
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

В корневой папке проекта введите команду для создания .env файла:

```py
echo '''DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
''' > .env
```
