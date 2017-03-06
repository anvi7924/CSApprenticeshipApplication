import psycopg2
import os

import sys

sys.path.append("..")


def delete_create_database():
    # with psycopg2.connect(database="postgres", user="annavillani", password="1239") as conn:
    with psycopg2.connect(database="postgres", user="postgres", password="password") as conn:
        with conn.cursor() as cur:
            # Explains why we do this - we cannot drop or create from within a DB transaction.
            # http://initd.org/psycopg/docs/connection.html#connection.autocommit
            conn.autocommit = True
            cur.execute("DROP DATABASE IF EXISTS ceasdb;")
            cur.execute("DROP USER IF EXISTS ceas;")

            cur.execute("CREATE DATABASE ceasdb;")
            cur.execute("CREATE USER ceas WITH PASSWORD 'ceas';")
            cur.execute("ALTER ROLE ceas SET client_encoding TO 'utf8';")
            cur.execute("ALTER ROLE ceas SET default_transaction_isolation TO 'read committed';")
            cur.execute("ALTER ROLE ceas SET timezone TO 'UTC';")
            cur.execute("GRANT ALL PRIVILEGES ON DATABASE ceasdb TO ceas;")


def delete_migration_files():
    folder = os.path.abspath(os.path.curdir)
    print(folder)
    for file in os.listdir(os.path.join(folder, "migrations")):
        if file.endswith(".py"):
            if file != "__init__.py":
                os.remove(os.path.join(folder, "migrations", file))


def make_migrations():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CEAS_website.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(['manage.py', 'makemigrations'])
    execute_from_command_line(['manage.py', 'migrate', 'auth'])
    execute_from_command_line(['manage.py', 'migrate'])


def create_superuser():
    from django.contrib.auth.models import User
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CEAS_website.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    # execute_from_command_line(sys.argv)
    User.objects.create_superuser('ken', 'admin@example.com', 'professore')


def db_backup(filename):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CEAS_website.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    original_stdout = sys.stdout
    f_handler = open(filename, 'w')
    sys.stdout = f_handler

    execute_from_command_line(['manage.py', 'dumpdata'])

    sys.stdout = original_stdout
    f_handler.close()


def db_restore(filename):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CEAS_website.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(['manage.py', 'loaddata', filename])


if __name__ == '__main__':
    # delete_create_database()
    # delete_migration_files()
    # make_migrations()
    # create_superuser()

    db_backup("db.json")
    db_restore("db.json")
