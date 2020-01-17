# twotickets


# requirement :

1 - install psycopg2:
`pip install psycopg2`

2 - install django.filter:
`pip install django.filter`

3 - install postgresql:
`https://www.postgresql.org/`

4 - create postgres database called DB.

5 - copy git repository where you want:
`git clone https://github.com/boko911/twotickets.git`

6 - make the migration
`python manage.py migrate`

7 - load data from jsonfile
`python manage.py loaddata pizzeria/fixtures/load_pizzas.json`

8 - launch the app from Coding folder:
`python manage.py runserver`

