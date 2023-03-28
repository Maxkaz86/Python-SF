import telebot
from config import keys, TOKEN
from utils import APIException, ExchangeConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_request(message):
    text = 'Привет! Чтобы узнать курс интересующей Вас валюты введите запрос в формате:\n ' \
           '<имя валюты для конвертации>' \
           '<в какую валюту конвертировать>' \
           ' <количество>\n' \
           'Увидеть список всех доступных валют: /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        value = message.text.split(' ')
        if len(value) != 3:
            raise APIException('Указано слишком много параметров')

        quote, base, amount = value
        quote_ticker = keys[quote]
        base_ticker = keys[base]
        total_base = ExchangeConverter.convert_check(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote_ticker} в {base_ticker} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()