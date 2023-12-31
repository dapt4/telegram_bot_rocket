import time
from io import BytesIO
import requests


def singleton(func):
    instances = {}
    def empty_func():
        pass
    def get_instance(*args, **kwargs):
        if func not in instances:
            instances[func] = func(*args, **kwargs)
            return instances[func]
        else:
            return empty_func()
    return get_instance

@singleton
def polling_threadF(bot_instance):
    '''
    to start the connection with the bot once
    '''
    bot_instance.infinity_polling(none_stop=True)


def bisection(a, b):
    '''
    to calculate the next number
    '''
    tolerance = 0.5
    if (b - a) / 2.0 > tolerance:
        c = (a + b) // 2
        return c, False
    result = (a + b) // 2
    return result, True


def timestamp_date(timestamp):
    '''
    to convert timestamps to readable date
    '''
    fecha = time.strftime("%Y-%m-%d", time.gmtime(timestamp))
    return fecha


def result_message(bot_instance, message, frame, index, date):
    '''
    To send a message with the result to the user
    '''
    bot_instance.reply_to(message, f'Found! Take-off = {frame}, in {index} steps at {date}')


def send_photo(bot_instance, id, frame, index):
    '''
    To download and send the photos to the user
    '''
    try:
        url = f'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20%28Hosted%20Webcast%29-wbSwFU6tY1c/frame/{frame}/'
        bot_instance.send_photo(id, url, caption=f'{index} - {frame} - did the rocket launch yet?[y/n]')
        return True
    except Exception:
        return False


