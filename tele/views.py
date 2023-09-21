from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
import telebot
import requests
from io import BytesIO
import os
import threading
from .utils import polling_threadF, bisection
from .models import Chat
import traceback


global TOKEN
TOKEN = os.environ.get('bot_token')
global bot
bot = telebot.TeleBot(TOKEN)
global URL
URL = os.environ.get('URL')


polling_thread = threading.Thread(target=polling_threadF, args=(bot,))
polling_thread.start() # uncoment for production


# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'for start use /start')


@bot.message_handler(commands=['start'])
def start(message):
    try:
        chat = Chat.objects.get(user_id=message.chat.id)
        if chat is not None:
            chat.delete()
    except Exception as e:
        traceback.print_exc()
    try:
        frame, done = bisection(0, 61695, None)
        index = 1
        url = f'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20%28Hosted%20Webcast%29-wbSwFU6tY1c/frame/{frame}/'
        response = requests.get(url)
        if response.status_code == 200:
            chat = Chat(user_id=message.chat.id, bottom=0, middle=frame, top=61695, index=index, date=message.date )
            chat.save()
            image_bytes = BytesIO(response.content)
            bot.send_photo(chat.user_id, image_bytes, caption=f'{index} - {frame} - did the rocket launch yet?')
        else:
            bot.send_message(message.chat.id, f'Could not download the image from the url: {url}')
    except Exception as e:
        traceback.print_exc()
        bot.send_message(message.chat.id, f'An error occurred: {str(e)}')


@bot.message_handler(func = lambda message:True)
def receive_response(message):
    response = message.text.lower()
    try:
        chat = Chat.objects.get(user_id=message.chat.id)
        index = chat.index + 1
        frame: int
        done: bool
        if response == 'y':
            frame, done = bisection(chat.bottom, chat.middle, response)
            if done:
                return bot.reply_to(message, f'Found! Take-off = {frame}, in {chat.index}')
            chat.top = chat.middle
            chat.middle = frame
            chat.index = index
            chat.date = message.date
            chat.save()
        else:
            frame, done = bisection(chat.middle, chat.top, response)
            if done:
                return bot.reply_to(message, f'Found! Take-off = {frame}, in {chat.index}')
            chat.bottom = chat.middle
            chat.middle = frame
            chat.index = index
            chat.date = message.date
            chat.save()
        url = f'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20%28Hosted%20Webcast%29-wbSwFU6tY1c/frame/{frame}/'
        response = requests.get(url)
        if response.status_code == 200:
            image_bytes = BytesIO(response.content)
            bot.send_photo(chat.user_id, image_bytes, caption=f'{index} - {frame} - did the rocket launch yet?')
    except Exception as exc:
        traceback.print_exc()
        bot.send_message(message.chat.id, f'An error occurred: {str(exc)}')




