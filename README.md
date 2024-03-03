pip install poetry

git clone https://github.com/dominikszopa/fundraising.git

go to fund-raising website

poetry install

poetry shell

cp .env.example .env

change the credentials

python manage.py migrate

python manage.py loaddata startingdata

python manage.py runserver

localhost:8000
