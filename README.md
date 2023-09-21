# backend_with

## requirements

- python3.10
- pyenv if you dont have 3.10 version
- poerty or pip
- ngrok


## setup

- the dependencies are handled with poerty by default, but you can use pip if you prefer

`$ poerty install`

- or 

`$ pip install -r requirements.txt`

- create a virtual env and active activet it

`$ poetry shell`

- or

`$ python -m venv venv`
`$ source venv/bin/activate`

- create a file .env and add your credentials 

>ENV_SECRET_KEY="{add a secret key like bhajfbkjhawbdkjhabdjh}"\
bot_token = '{your token (botFather bot provide it to you)}'\
URL = '{the public url (ngrok provide it to you)}'

- migrate the app

`$ python manage.py migrate`

- run the command:

`$ python manage.py migrate`

## run the app

`$ ngrok http 8000`

- get the public url from ngrolk cli in the line:

`Forwarding                    https://cecf-2-155-157-182.ngrok-free.app -> http://localhost:8000`

- paste it in the URL variable of the .env file, like this:

`URL = 'cecf-2-155-157-182.ngrok-free.app'`

- run the server

`$ python manage.py runserver`

## try the app

- open telegram, go to the finder and search:

`rocketDiegoPerozobot`

- select and click in "start" button

## commands

`/help` - for instructions

`/start` - for init the app

- then follow the instructions
