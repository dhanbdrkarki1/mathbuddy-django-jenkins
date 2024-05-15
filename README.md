# MathBuddy

### Cloning the repository

--> Clone the repository using the command below :

```bash
git clone https://github.com/dhanbdrkarki1/mathbuddy-cloud.git

```

--> Move into the directory where we have the project files :

```bash
cd mathbuddy-cloud
```

--> Create a virtual environment :

# install virtualenv first

```bash
python -m pip install virtualenv
```

# create virtual environment

```bash
virtualenv venv

```

--> Activate the virtual environment :

```bash
venv\scripts\activate
```

--> Install the requirements :

```bash
python -m pip install -r requirements.txt

```

#

### Database Setup for localhost

--> Open xampp server & start apache and mysql.

--> Click on admin button in the mysql row to open UI

--> Click New then, give 'mathbuddy' as database name then, click create.

--> Click on import from the UI.

--> Choose file: mathbuddy.sql and the click import.

#

### Running the App

--> To run the App, we use :

```bash
python manage.py runserver

```

> ⚠ Open the link in browser: http://127.0.0.1:8000/


# Dockerizing
