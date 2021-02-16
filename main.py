#!/usr/bin/env python
# -*- coding: utf-8 -*-
from vt import *
import config
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import time
v = vt()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    v.Create_table()
    if v.check_rss() == True:
        v.write_log('İnfo', 'App runing')
        update.message.reply_text("App Runing...")

    else:
        update.message.reply_text('Not added rss, please first add rss')
        v.write_log('Error', 'App not start, because not have rss link')


def get_job(update, context):
    a = len(vt().fetch_data())
    if a > 0:
        v.write_log('Send Job', str(a) + ' Job sended')
        update.message.reply_text('----- Since the last posting ' + str(a) + ' more jobs have been added -----')
        time.sleep(2)
    else:
        update.message.reply_text('No new jobs have been added since the last post')

    while a > 0:
        b = vt().fetch_data()[a - 1][0]
        update.message.reply_text(str(vt().fetch_data()[a - 1][0]) +" " + vt().fetch_data()[a - 1][1])  # id
        time.sleep(0.5)
        a -= 1
        vt().change(b)

def get_log(update,context):
    row = context.args[0]
    a = len(vt().read_log(row))
    update.message.reply_text(" -- last " + row + " record will show. Just wait a moment ")
    time.sleep(3)
    while a > 0:
        update.message.reply_text("id: " + str(vt().read_log(row)[a - 1][0]) +" --> " + vt().read_log(row)[a - 1][2]+ " - " + vt().read_log(row)[a - 1][3])
        a -= 1
        time.sleep(0.5)


def get_specific(update, context):
    id = context.args[0]
    field = context.args[1]
    if field == "title":
        update.message.reply_text(str(v.search_id(id)[0][0]) + " " + v.search_id(id)[0][1])
        time.sleep(0.5)
    elif field == "content":
        update.message.reply_text(v.search_id(id)[0][2])
        time.sleep(0.5)
    elif field == "link":
        update.message.reply_text(v.search_id(id)[0][4])
        time.sleep(0.5)
    else:
        update.message.reply_text('Wrong wrote, please try again')

def add_rss(update, context):
    rss = context.args[0]
    v.add_rss(rss)
    update.message.reply_text('Rss Added')


def deljob(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Yes", callback_data='1'),
            InlineKeyboardButton("No", callback_data='2'),
        ],
        [InlineKeyboardButton("Cancel", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Are you sure ?, İf your answer yes, will delete all job ?:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == '1':
        v.deljob()
        query.edit_message_text('Dell all job succesfull')
        v.write_log('info','Deleted all job')
    elif query.data == '2':
        query.edit_message_text('Selected No')
    elif query.data == '3':
        query.edit_message_text('Cancel')

def help(update, context):
    update.message.reply_text('Welcome to Upwork job sender! \n 1- For take job "/getjob" \n 2- For take detail "/get {job_id} {title or content or link}. Need two argument!" \n 3- For delete job /deljob "its delete full job on database \n 4- For add rss /addrss {rss link here} \n 5- For read log /getlog')



def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    v.Create_table()
    updater = Updater(config.bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("getjob", get_job))
    dp.add_handler(CommandHandler("get", get_specific))
    dp.add_handler(CommandHandler("addrss", add_rss))
    dp.add_handler(CommandHandler("deljob", deljob))
    dp.add_handler(CommandHandler("getlog", get_log))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler("help", help))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

