import telebot

from src.constants import *

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, start_text)
    bot.send_message(message.chat.id, "You have written " + message.text)

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Начать игру!")
    markup.add(item1)		


bot.polling(none_stop = True)
