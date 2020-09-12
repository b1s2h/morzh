import telebot
import random
 
from telebot import types
a=['Орёл', 'Решка']


bot = telebot.TeleBot('1224283357:AAEdnAoFaLeHDlPH4TJ_HkIE3AZfCRvzPHQ')


@bot.message_handler(commands=['info'])
def bio (message):
 bot.send_message(message.chat.id, 'Гой Гайа! Я тупой бот Морж, меня создал всемогущий mmendel_613. Я могу зароллить число от 1 до 100 командой /roll, также могу бросить монетку командой /money.')
 

@bot.message_handler(commands=['money'])
def money(message):
  bot.send_message(message.chat.id, str(random.choice(a)))


@bot.message_handler(commands=['roll'])
def roll(message):
  bot.send_message(message.chat.id, str(random.randint(0,100)))

bot.polling(none_stop=True)
