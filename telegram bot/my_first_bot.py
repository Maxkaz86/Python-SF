import telebot
from config import keys, TOKEN
from exstansions import APIexception, Exchangeconverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_request(message):
    text = 'Привет! Чтобы узнать курс интересующей Вас валюты введите запрос в формате:\n ' \
           '<имя валюты для конвертации>' \
           ' <в какую валюту конвертировать>' \
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
            raise APIexception('Указано слишком много параметров')

        base, quote, amount = value
        base_ticker = keys[base]
        quote_ticker = keys[quote]
        total_base = Exchangeconverter.get_price(base, quote, amount)
    except APIexception as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base_ticker} в {quote_ticker} - {int(total_base) * int(amount)}'
        bot.send_message(message.chat.id, text)

bot.polling()