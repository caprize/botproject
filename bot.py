import telebot
from telebot.types import Message

TOKEN = '731947153:AAETaq49IdPhGCg9YssRF6RmW3ZIjzAdX4o'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message:True)
def upper(message: Message):
    bot.reply_to(message, "Дарова)0))")


bot.polling()
