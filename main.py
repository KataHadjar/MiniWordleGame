import os
import telebot

from src.constants import *
from src.game_realisation import *

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

word_dict = ["", 0]


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, START_TEXT)
    word_dict[0] = ""
    word_dict[1] = 0


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, HELP_TEXT)
    word_dict[0] = ""
    word_dict[1] = 0


@bot.message_handler()
def game_message(message):
    if word_dict[0] == "":
        if (len(message.text) >= 2 or
                message.text < '3' or
                message.text > '9'):
            bot.send_message(message.chat.id,
                             'Введите корректную длину слова (от 3 до 9)')
        else:
            word_dict[0] = random_word(int(message.text))
            bot.send_message(message.chat.id,
                             'Вы выбрали длину слова ' + message.text + '. Можете начинать игру)')
    else:
        result = get_match(message.text, word_dict[0])
        if result[0] == 'П':
            bot.send_message(message.chat.id,
                             result + '. Вам потребовалось ' + str(word_dict[1] + 1) + ' попыток.')
            bot.send_message(message.chat.id, 'Для того, чтобы начать новую игру, введите длину нового слова)')
            word_dict[0] = ""
            word_dict[1] = 0
        else:
            bot.send_message(message.chat.id, result)
        if result[0] == 'Б':
            word_dict[1] += 1


bot.infinity_polling()
