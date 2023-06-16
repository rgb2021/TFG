import telebot

bot = telebot.TeleBot("6292498094:AAHXGl9edhnV93A6vrywDBCMpr-kvar4Tjc")

@bot.message_handler(commands=['saludo'])
def send_welcome(message):
	bot.reply_to(message, "case cabesa!")

@bot.message_handler(commands=['adios'])
def send_welcome(message):
        bot.reply_to(message, "sayonara baby!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "ni idea que es " + message.text)

bot.infinity_polling()
