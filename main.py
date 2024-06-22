import telebot
from telebot import types

bot = telebot.TeleBot('7360334831:AAFHK7hUgud6gtYBh6HfeG7YU-xMpPLRolA')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для конвертации чисел. \nПеревести в евро -> /eur кол-во рублей. \nПеревести в доллары -> /usd кол-во рублей. \nПеревести в юани -> /cny кол-во рублей. \nПеревести в тенге -> /kzt кол-во рублей. \nПеревести в лиры -> /try кол-во рублей. \nПеревести в баты -> /thb кол-во рублей. \nПеревести в дирхамы -> /aed кол-во рублей. \n Перевести в шекели -> /ils кол-во рублей. \nПеревести в шв. франки - /chf кол-во рублей")

@bot.message_handler()
def send_welcome(message):
     s = message.text
     if s.startswith('/eur'):
         symbols_to_remove = "/eur "

         for symbol in symbols_to_remove:
             s = s.replace(symbol, "")
         d = float(s)
         result = d / 94.25
         bot.reply_to(message, "Вы получите столько евро ")
         bot.reply_to(message, {result})
     else:
         s = message.text
         if s.startswith('/usd'):
             symbols_to_remove = "/usd  "

             for symbol in symbols_to_remove:
                 s = s.replace(symbol, "")
             d = float(s)
             result = d / 88.15
             bot.reply_to(message, "Вы получите столько долларов ")
             bot.reply_to(message, {result})
         else:
             s = message.text
             if s.startswith('/cny'):
                 symbols_to_remove = "/cny  "

                 for symbol in symbols_to_remove:
                     s = s.replace(symbol, "")
                 d = float(s)
                 result = d / 12.14
                 bot.reply_to(message, "Вы получите столько юаней ")
                 bot.reply_to(message, {result})
             else:
                 s = message.text
                 if s.startswith('/kzt'):
                     symbols_to_remove = "/kzt  "

                     for symbol in symbols_to_remove:
                         s = s.replace(symbol, "")
                     d = float(s)
                     result = d / 0.19
                     bot.reply_to(message, "Вы получите столько тенге ")
                     bot.reply_to(message, {result})
                 else:
                     s = message.text
                     if s.startswith('/try'):
                         symbols_to_remove = "/try  "

                         for symbol in symbols_to_remove:
                             s = s.replace(symbol, "")
                         d = float(s)
                         result = d / 2.69
                         bot.reply_to(message, "Вы получите столько лир ")
                         bot.reply_to(message, {result})
                     else:
                         s = message.text
                         if s.startswith('/thb'):
                             symbols_to_remove = "/thb  "

                             for symbol in symbols_to_remove:
                                 s = s.replace(symbol, "")
                             d = float(s)
                             result = d / 2.40
                             bot.reply_to(message, "Вы получите столько бат ")
                             bot.reply_to(message, {result})
                         else:
                             s = message.text
                             if s.startswith('/aed'):
                                 symbols_to_remove = "/aed "

                                 for symbol in symbols_to_remove:
                                     s = s.replace(symbol, "")
                                 d = float(s)
                                 result = d / 24
                                 bot.reply_to(message, "Вы получите столько дирхам ")
                                 bot.reply_to(message, {result})
                             else:
                                 s = message.text
                                 if s.startswith('/ils'):
                                     symbols_to_remove = "/ils "

                                     for symbol in symbols_to_remove:
                                         s = s.replace(symbol, "")
                                     d = float(s)
                                     result = d / 23.63
                                     bot.reply_to(message, "Вы получите столько шекелей ")
                                     bot.reply_to(message, {result})
                                 else:
                                     s = message.text
                                     if s.startswith('/chf'):
                                         symbols_to_remove = "/chf "

                                         for symbol in symbols_to_remove:
                                             s = s.replace(symbol, "")
                                         d = float(s)
                                         result = d / 98.65
                                         bot.reply_to(message, "Вы получите столько швейцарских франков ")
                                         bot.reply_to(message, {result})




# Запуск бота
bot.polling()


