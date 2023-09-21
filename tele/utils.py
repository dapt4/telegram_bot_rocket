def polling_threadF(bot_instance):
    bot_instance.remove_webhook()  # Elimina cualquier webhook existente
    bot_instance.polling()
    print('threading the bot.polling') # hacer algun log que me diga si esta corriendose este codigo mas de una vez, porque puede crear treads infinitos


def bisection(a, b, res):
    tolerance = 0.0001
    if (b - a) / 2.0 > tolerance:
        print("entro aqui")
        c = (a + b) // 2
        '''
        if res and res == 'y':
            b = c
        elif res != 'y' and res != None:
            a = c
        else:
            return (c, False)'''
        return c, False
    print("acá")
    number = (a + b) // 2
    return number, True

