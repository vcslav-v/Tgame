from telebot import types
from app import models
from app import db
import json


def poster(bot, chatId, text=None, buttons=None, ed=False, message_id=None, doc=None, img=None):
    if buttons:
        if ed and not img and not doc:
            bot.edit_message_text(chat_id=chatId, message_id=message_id, text=text, reply_markup=inlineKeyboarder(buttons))
        else:
            if img:
                bot.send_photo(chat_id=chatId, photo=img, reply_markup=inlineKeyboarder(buttons))
            if text:
                bot.send_message(chatId, text, reply_markup=inlineKeyboarder(buttons))
            if doc:
                bot.send_document(chat_id=chatId, data=doc, reply_markup=inlineKeyboarder(buttons))
    else:
        if ed and not img and not doc:
            bot.edit_message_text(chat_id=chatId, message_id=message_id, text=text)
        else:
            if img:
                bot.send_photo(chat_id=chatId, photo=img)
            if text:
                bot.send_message(chatId, text)
            if doc:
                bot.send_document(chat_id=chatId, data=doc)

def inlineKeyboarder(keys):
    keyboard = types.InlineKeyboardMarkup()
    for key in keys:
        keyboard.add(types.InlineKeyboardButton(text=key, callback_data=json.dumps(keys[key])))
    return keyboard

def keyboarder(keys):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    temp = []
    for i in keys:
        temp.append(i)
    temp.reverse()
    for i in temp:
        keyboard.add(i)
    return keyboard