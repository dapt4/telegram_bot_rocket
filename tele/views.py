from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
import telebot
import os
import threading
from .utils import polling_threadF, bisection, send_photo, result_message
from .models import Chat
import traceback
from .utils import timestamp_date

global TOKEN
TOKEN = os.environ.get('bot_token')
global bot
bot = telebot.TeleBot(TOKEN)


polling_thread = threading.Thread(target=polling_threadF, args=(bot,))
polling_thread.start()


# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    '''
    for load a template
    '''
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))


@bot.message_handler(commands=['help'])
def help(message):
    '''
    for send a message to start the bot
    '''
    bot.reply_to(message, 'for start use /start')


@bot.message_handler(commands=['start'])
def start(message):
    '''
    this is the start function of the bot
    '''
    try:
        chat = Chat.objects.get(user_id=message.chat.id)
        if chat is not None:
            chat.delete()
    except Exception as e:
        traceback.print_exc()
    try:
        frame, done = bisection(0, 61695)
        index = 1
        if send_photo(bot, message.chat.id, frame, index):
            chat = Chat(user_id=message.chat.id, bottom=0, middle=frame, top=61695, index=index, date=message.date )
            chat.save()
        else:
            bot.send_message(message.chat.id, f'Could not download the image from the url: {url}')
    except Exception as e:
        traceback.print_exc()
        bot.send_message(message.chat.id, f'An error occurred: {str(e)}')


@bot.message_handler(func = lambda message:True)
def receive_response(message):
    '''
    receive responses and processes them
    '''
    response = message.text.lower()
    try:
        chat = Chat.objects.get(user_id=message.chat.id)
        index = chat.index + 1
        frame: int
        done: bool
        if response == 'y':
            frame, done = bisection(chat.bottom, chat.middle)
            if done:
                return result_message(bot, message, frame, chat.index, timestamp_date(chat.date))
            chat.top = chat.middle
            chat.middle = frame
            chat.index = index
            chat.date = message.date
            chat.save()
        else:
            frame, done = bisection(chat.middle, chat.top)
            if done:
                return result_message(bot, message, frame, chat.index, timestamp_date(chat.date))
            chat.bottom = chat.middle
            chat.middle = frame
            chat.index = index
            chat.date = message.date
            chat.save()
        if not send_photo(bot, chat.user_id, frame, index):
            bot.send_message(message.chat.id, f'Could not download the image from the url: {url}')
    except Exception as exc:
        traceback.print_exc()
        bot.send_message(message.chat.id, f'An error occurred: {str(exc)}')




