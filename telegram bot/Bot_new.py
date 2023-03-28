# import telebot
#
# TOKEN = '6237997648:AAEdjVDUf2dt96F-GNTVsY1ZsGGdL4idOcU' #добавил токен полученный при создании бота
#
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f'Welcome, {message.chat.username}')
#
# @bot.message_handler(content_types=['photo'])
# def message_handler(message: telebot.types.Message):
#     bot.reply_to(message, f'Отличный мем {message.from_user.first_name}')
#
#
# bot.polling(non_stop=True) #запуск бота, параметр говорит о том, что бот должен быть активен при любых ошибках