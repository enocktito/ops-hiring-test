===========
Event API
===========

Setup
======

1. Create virtual environment::

    virtualenv --python=python3.7 venv

2. Activate virtual environment::

    source venv/bin/activate

3. Install dependencies::

    pip install -r requirements.txt

4. Create media root directory::

    mkdir -p /var/www/kele/media
    chmod -R 777 /var/www/kele/

5. Define the **JWT_SECRET** env var. Refer to this link https://www.grc.com/passwords.htm.

6. Run migrations::

    python manage migrate

7. Setup your env var for the db `settings.py` and add DB_USER and DB_PASSWORD in your env::

    DB_NAME: Database name
    DB_USER: Database user
    DB_PASSWORD: Database password

8. Créer un schema `event`

9. Run server::

    python manage runserver


NB
--
The database used is `postgres-11.5`.

For the moment, `mysql` or `sqlite3` can work with migrations

