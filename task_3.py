# Создать телелеграм-бота калькулятор с инлайн-клавиатурой.
# Бот должен запрашивать угол. С помощью модуля математики создать кнопки на инлайн-клавиатуре,
# с помощью которых можно посчитать синус, косинус и тангенс для введенного угла (sin, cos, tan).
# Все необходимые модули рассматриваются в методичках.

import math
import telebot
from telebot import types

TOKEN = "5774051177:AAHsT6m-DTl9Gjn0BmKN2uXie9hRWEuD0L8"

bot = telebot.TeleBot(TOKEN)

user_dict = {}


class User:
    def __init__(self, requested_number):
        self.requested_number = requested_number


@bot.message_handler(commands=["start"])
def send_welcome(message):
    msg = bot.reply_to(message, """\
        Hi there, I am a math bot.
        What's your number?
    """)

    bot.register_next_step_handler(msg, choose_math_action)


def choose_math_action(message):
    try:
        requested_number = int(message.text)
        user = User(requested_number)
        user_dict["user"] = user
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        button_sin = types.InlineKeyboardButton("sin", callback_data='sin')
        button_cos = types.InlineKeyboardButton("cos", callback_data='cos')
        button_tan = types.InlineKeyboardButton("tan", callback_data='tan')
        keyboard.add(button_sin, button_cos, button_tan)
        bot.send_message(message.chat.id, 'Choose math action', reply_markup=keyboard)
    except Exception as e:
        bot.reply_to(message, f'oooops {e}')


@bot.callback_query_handler(func=lambda message: True)
def logic_inline(call):
    result = None
    if call.data == 'sin':
        result = math.sin(user_dict["user"].requested_number)
    elif call.data == 'cos':
        result = math.cos(user_dict["user"].requested_number)
    elif call.data == 'tan':
        result = math.tan(user_dict["user"].requested_number)
    result = str(result)
    bot.send_message(call.message.chat.id, result)


bot.infinity_polling()
