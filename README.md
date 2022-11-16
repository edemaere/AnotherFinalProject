# AnotherFinalProject

I decided to make a fresh wipe of what the project was before I turned it to scrambled eggs, then carefully added templates, models, and database settings. I think the thing that was making things difficult was trying to make a bootstrap template work with django (which is possible, just time consuming and frustrating).

I focused on just making what Part 2 asks for:

- Create the database in PostgreSQL *(DONE, see step 3)*
- Create the necessary templates *(these are currently very empty, but they exist)*
- Create the necessary models and map to the database *(DONE, see step 4)*
- Define Django forms used in the project. You do not need to create them yet *(haven't gotten to this yet)*
- Create an Admin interface that works with the models *(DONE? see step 5)*

### Steps for setting up the project

1. Clone  the repository.
2. Make sure django and psycopg2 are installed (run "pip install django" and "pip install psycopg2" if they aren't).
3. The project is currently built to connect to a database called "fitness" (you can find this setting in "admin/settings.py" on the DATABASES section). If you already have pgAdmin set up, start a SQL Shell (psql) and enter the password you used for pgAdmin. Once you're in, run "create database fitness;". This will make the database for the project.
4. Run "python manage.py migrate". It will ask you for a password - this is for the database, same password used for pgAdmin (the password prompt was setup using the getpass() function in the DATABASES settings). After entering your password, the database schema will be mapped to the database (setup for the schema is in "GainPages/models.py").
5. Run "python manage.py createsuperuser" to make an admin account for managing the database.
6. Finally, you can run "python manage.py runserver". It will prompt twice for the database password before starting.

### What's Next:

The html templates need to be designed.
