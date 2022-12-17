# Создать телеграм-бота с инлайн-клавиатурой.
#
# Бот должен создавать нового игрового персонажа. Должен запросить: имя игрока, тип игрока (две кнопки на клавиатуре).
#
# Должен присвоить ему рандомные характеристики(здоровье, сила).
#
# После создания игрока нужно вывести на экран сообщение с его данными.
#
# Игрок должен создаваться с помощью класса.


import telebot
from random import randrange
from telebot import types


class Player:
    def __init__(self):
        self.name = None
        self.type = None
        self.health = randrange(100, 150)
        self.strength = randrange(20, 50)


player = Player()
bot = telebot.TeleBot('5873858262:AAGTXruVTAtUS-V9k2K95fXVqK5kjc_7SVg')
flag = ''


@bot.message_handler(commands=['start', 'help'])
def bein(message):
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup()
        key_name = types.InlineKeyboardButton(text='Имя', callback_data='key_name')
        key_type = types.InlineKeyboardButton(text='Тип игрока', callback_data='key_type')
        keyboard.add(key_name, key_type)
        bot.send_message(message.chat.id, text='Привет! Давай создадим игрока', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, text='Этот бот предназначен для создания игрока')


@bot.callback_query_handler(func=lambda call: True)
def call_et(call):
    global flag
    if call.data == 'key_name':
        flag = 'name'
        bot.send_message(call.message.chat.id, text='Введите имя игрока')
    elif call.data == 'key_type':
        flag = 'type'
        bot.send_message(call.message.chat.id, text='Введите тип игрока')


@bot.message_handler(content_types=['text'])
def text(message):
    global flag
    if flag == 'name':
        player.name = message.text
    elif flag == 'type':
        flag = ''
        player.type = message.text
        bot.send_message(message.chat.id, text=f'Имя: {player.name}\nТип: {player.type}\nЗдоровье: {player.health}\n'
                                               f'Сила: {player.strength}')
    else:
        bot.send_message(message.chat.id, text='Нажми /help')


bot.polling(non_stop=True)
