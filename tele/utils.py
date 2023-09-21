def polling_threadF(bot_instance):
    bot_instance.remove_webhook()  # Elimina cualquier webhook existente
    bot_instance.polling()
    print('threading the bot.polling') # hacer algun log que me diga si esta corriendose este codigo mas de una vez, porque puede crear treads infinitos



