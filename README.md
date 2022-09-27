# Luad Game Lottery System Headless API

This application enables Django powered websites to have multiple tenants via PostgreSQL schemas. A vital feature for every Software-as-a-Service website.
        
    # Creat a new database
    CREATE DATABASE 'luad_game'


### Basic Settings for Development
Activate environment

    python  -m venv  venv
    source venv/bin/activate

Install dependencies

    pip install -r requirements_dev.txt


Basic Settings
You’ll have to make the following creations to your your .env file
and Django Secret Key


    DB_NAME=your_database_name
    DB_USR=your_user_name
    DB_PWD=your_password

    SECRET_KEY='your_secret_key'

Your DATABASE_ENGINE setting (luad_game/settings.py) needs to be changed to

    DATABASES = {
    'default': {
            # Tenant Engine
            'ENGINE': 'django.postgresql_backend',
            # set database name
            'NAME': 'your_db_name',
            # set your user details
            'USER': 'your_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'POST': '5432'
        }
    }

Make migrations and Apply to database

    # create migrations files (every new django app)
    python manage.py makemigrations
    python manage.py makemigrations lottery
    # Apply migrations
    python manage.py migrate
    # collect static files
    python manage.py collectstatic 

To set up Lao language, it is required gettext library:

For Ubuntu:

    sudo apt install -y gettext

For Mac:

    Brew install gettext


Setup Initial User, and Admin
        
    # create first user
    python manage.py createsuperuser
    python manage.py runserver

Go to
    localhost:8000/admin/ or localhost:8000/swagger/

For Checking before deploy
    
    # API/ Unit Test
    python manage.py test
        
    # Deploy checklist
    python manage.py check --deploy

    # Check Style
    pip install flake8
    flake8 martor_demo/ --max-line-length=127


### Setting for Production to Google Cloud Run with Google SQL and Google Storage
Create environment file .env_prod in root folder with follow settings:

    USE_CLOUD_SQL_AUTH_PROXY=True
    GOOGLE_CLOUD_PROJECT=Your Project
    GOOGLE_APPLICATION_CREDENTIALS=your credentail file

Andc create another global enviroment .global_env_prod.sh

    #!/bin/bash
    export SECRET_KEY=your secret key
    export DATABASE_URL=your database url 
    export GS_BUCKET_NAME=your bucket name
    export CLOUD_RUN_URL=your cloud run generated url


Export Global Variable

    source .global_env_prod.sh

Change Project Settings pointer luad_game_core/wsgi.py and luad_game_core/asgi.py

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luad_game_core.settings_prod')


    ### Basic setting for deployment
    To run by using Docker 
    
    # Build Docker images
    docker build -t your_cloud_container_registry/your_container_name:your_version . --network=host

    # Run Docker container
    docker run -p 8000:8000 #image_id --network=host

    # Push container to Cloud
    gcloud docker -- push our_cloud_container_registry/your_container_name:your_version
