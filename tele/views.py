from rest_framework.decorators import api_view
import telebot
import requests
from io import BytesIO
import os
import threading
from .utils import polling_threadF


global TOKEN
TOKEN = os.environ.get('bot_token')
global bot
bot = telebot.TeleBot(TOKEN)
global URL
URL = os.environ.get('URL')


polling_thread = threading.Thread(target=polling_threadF, args=(bot,))
polling_thread.start()


# Create your views here.
@api_view(['GET', 'POST'])
def index():
   return '.'


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'for start use /start')


@bot.message_handler(commands=['start'])
def start(message):
    try:
        index = 39554
        url = f'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20%28Hosted%20Webcast%29-wbSwFU6tY1c/frame/{index}/'
        response = requests.get(url)
        if response.status_code == 200:
            image_bytes = BytesIO(response.content)
            bot.send_photo(message.chat.id, image_bytes)
            bot.reply_to(message, f'{index} - did the rocket launch yet?')
        else:
            bot.send_message(message.chat.id, f'No se pudo descargar la imagen desde la url: {url}')
    except Exception as e:
            bot.send_message(message.chat.id, f'Ocurrió un error: {str(e)}')


@bot.message_handler(func = lambda message:True)
def receive_response(message):
    response = message.text
    if response.lower() == 'y':
        pass
    else:
        pass
    bot.reply_to(message, f'{1} - did the rocket launch yet?')




