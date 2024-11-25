run:
	python manage.py runserver

mkmigra:
	python manage.py makemigrations

migra:
	python manage.py migrate

static:
	python manage.py collectstatic
