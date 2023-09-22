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

`$ python -m venv venv`
`$ source venv/bin/activate`

- the dependencies are handled with poerty by default, but you can use pip if you prefer

`$ poerty install`

- or 

`$ pip install -r requirements.txt`


- create a file .env and add your credentials 

>ENV_SECRET_KEY="{add a secret key like bhajfbkjhawbdkjhabdjh}"\
bot_token = '{your token (botFather bot provide it to you)}'\
ENV_NAME = "rocket"\
ENV_HOST = "localhost"\ 
ENV_PORT = "5432"\
ENV_USER = "postgres"\
ENV_PASSWORD = "19570744"

- make the migrations 

`$ python manage.py makemigrations`

- run the command:

`$ python manage.py migrate`

## run the app

- uncomment this line (21) in views.py

`$ #polling_thread.start()`

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


