import os
import random
import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("pic")
    markup.add(item1)
    bot.send_message(message.chat.id,'hi!',reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="pic":
        rfile = ["./pics/", random.choice(os.listdir(path = './pics'))]
        photo = open("".join(rfile), 'rb')
        bot.send_photo( message.chat.id, photo )
        photo.close()
bot.infinity_polling()
