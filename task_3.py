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

#Todo ИНлайн клавиатура
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
        keyboard = types.InlineKeyboardMarkup()
        button_sin = types.KeyboardButton("sin")
        button_cos = types.KeyboardButton("cos")
        button_tan = types.KeyboardButton("tan")
        keyboard.add(button_sin, button_cos, button_tan)
        msg = bot.reply_to(message, text="Choose math action", reply_markup=keyboard)
        bot.register_next_step_handler(msg, doing_math)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def doing_math(message):
    result = None
    if message.text == "sin":
        result = math.sin(user_dict["user"].requested_number)
    elif message.text == "cos":
        result = math.cos(user_dict["user"].requested_number)
    elif message.text == "tan":
        result = math.tan(user_dict["user"].requested_number)

    result = str(result)
    bot.reply_to(message, result)


bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.infinity_polling()

