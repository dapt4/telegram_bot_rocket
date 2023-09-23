# backend_with

## requirements

- python3.10
- pyenv if you dont have 3.10 version
- poerty or pip
- ngrok


## setup

- create a virtual env and active activet it

`$ poetry shell`

- or

`$ python -m venv venv`\
`$ source venv/bin/activate`

- the dependencies are handled with poerty by default, but you can use pip if you prefer

`$ poerty install`

- or 

`$ pip install -r requirements.txt`


- create a file .env and add your credentials 

>ENV_SECRET_KEY="{add a secret key like bhajfbkjhawbdkjhabdjh}"\
bot_token = '{your token (botFather bot provide it to you)}'\
URL = "{add URL or IP of the hosting}"
ENV_NAME = "{database name}"\
ENV_HOST = "{localhost or  DB path }"\ 
ENV_PORT = "{5432 or your custom Port }"\
ENV_USER = "{db user}"\
ENV_PASSWORD = "{db password}"\

- make the migrations 

`$ python manage.py makemigrations`

- run the command:

`$ python manage.py migrate`

## run the app

- run the following command with the same port of django (8000)

`$ ngrok http 8000`

- run the server

`$ python manage.py runserver`

## try the app

- open telegram, go to the finder and search:

`rocket_by_diego_perozo`

- or use the following link

`https://t.me/rocketDiegoPerozobot`

- select and click in "start" button

## commands

`/help` - for instructions

`/start` - for init the app

- then follow the instructions


