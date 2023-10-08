import random
import types

import telebot

bot = telebot.TeleBot("токен", parse_mode=None)  # спрятать токен бота

rpc_game = "камень, ножницы, бумага"
cz_game = "крестики-нолики"

keyboard_game = telebot.types.ReplyKeyboardMarkup(True)
keyboard_game.row(rpc_game, cz_game)

keyboard_RPC = telebot.types.ReplyKeyboardMarkup(True)
keyboard_RPC.row("камень", "ножницы", "бумага")


@bot.message_handler(commands=['start', 'info'])
def send_welcome(message):
    bot.send_message(message.chat.id, "это тестовое приветсвие", reply_markup=keyboard_game)


@bot.message_handler(content_types=['text'])
def messages(message):
    user_choice = message.text
    options = ['камень', 'ножницы', 'бумага']
    bot_choice = options[random.randint(0, 2)]
    if (user_choice == "камень" and bot_choice == "бумага") or (
            user_choice == "ножницы" and bot_choice == "камень") or (
            user_choice == "бумага" and bot_choice == "ножницы"):
        bot.send_message(message.chat.id, "Поражение. Выбор бота: " + bot_choice, reply_markup=keyboard_RPC)
    elif (user_choice == "камень" and bot_choice == "ножницы") or (
            user_choice == "ножницы" and bot_choice == "бумага") or (
            user_choice == "бумага" and bot_choice == "камень"):
        bot.send_message(message.chat.id, "Победа. Выбор бота: " + bot_choice, reply_markup=keyboard_RPC)
    elif (user_choice == "камень" and bot_choice == "камень") or (
            user_choice == "ножницы" and bot_choice == "ножницы") or (
            user_choice == "бумага" and bot_choice == "бумага"):
        bot.send_message(message.chat.id, "Ничья " + bot_choice, reply_markup=keyboard_RPC)


bot.polling()
