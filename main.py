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

def check():
    if v.check_rss() == True:
        v.write_log('İnfo', 'App runing')
        return True
    else:
        v.write_log('Error', 'App not start, because not have rss link')
        return False

def start(update, context):
    if check():
        update.message.reply_text('Welcome to Upwork job sender, with this application, you can send the sources you follow to the telegram to read them at any time.')
        time.sleep(0.7)
        update.message.reply_text('App runing')
    else:
        update.message.reply_text('Welcome to Upwork job sender, with this application, you can send the sources you follow to the telegram to read them at any time.')
        time.sleep(0.7)
        update.message.reply_text('It looks like no rss has been added yet. Type the following to add')
        time.sleep(0.7)
        update.message.reply_text('/addrss {rss link here}')


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


def button_get_job(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'title':
        update.message.reply_text('title')
    elif query.data == 'content':
        update.message.reply_text('content')
    elif query.data == 'link':
        update.message.reply_text('link')

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
    field = context.args
    id = context.args[0]
    if len(field) == 1:
        update.message.reply_text(str(v.search_id(id)[0][0]) + " " + v.search_id(id)[0][1])
        time.sleep(0.5)
        update.message.reply_text(v.search_id(id)[0][2])
    elif len(field) == 2 and field[1] == "title":
        update.message.reply_text(str(v.search_id(id)[0][0]) + " " + v.search_id(id)[0][1])
        time.sleep(0.5)
    elif len(field) == 2 and field[1] == "content":
        update.message.reply_text(v.search_id(id)[0][2])
        time.sleep(0.5)
    elif len(field) == 2 and field[1] == "link":
        update.message.reply_text(v.search_id(id)[0][4])
        time.sleep(0.5)
    else:
        update.message.reply_text('Wrong wrote, please try again')


def direct_job(update: Update, context: CallbackContext) -> None:
    id = update.message.text
    if id.isdigit():
        update.message.reply_text(v.search_id(id)[0][1])
        time.sleep(0.5)
        update.message.reply_text(v.search_id(id)[0][2])
    else:
        update.message.reply_text("Wrong! if you want help, you can write /help")


def add_rss(update, context):
    rss = context.args[0]
    v.add_rss(rss)
    v.write_log('İnfo', 'Rss Added')
    update.message.reply_text('Rss Added')



def del_rss(update,context):
    if len(context.args) == 1:
        update.message.reply_text("This rss deleted > " + str(v.search_rss(context.args[0])[0][1]))
    else:
        co = 0
        lenn = len(v.show_all_rss())
        while lenn > co:
            id = v.show_all_rss()[co - 1][0]
            rss = v.show_all_rss()[co - 1][1]
            AddDate = v.show_all_rss()[co - 1][2]
            update.message.reply_text("id -- > " + str(id) + " | " + "Rss link --> " + rss + " | " + "Added Date --> " + AddDate)
            co += 1
            time.sleep(0.3)
        update.message.reply_text("If you want delete rss, please enter the id value " + " Etc.  /delrss {id}")
        update.message.reply_text("INFO! -- > Write just one id value if you want delete")

def addnote(update,context):
    lencon = len(context.args)
    title = context.args[0:1]
    note = context.args[1:lencon]
    data = ""
    for i in note:
        data += i + " "
    v.addnote(title[0], data)
    v.write_log('İnfo', 'Note Added')
    update.message.reply_text('Note Added')

def shownote(update,context):
    lendata = len(v.fetch_note())
    update.message.reply_text('Your have : ' + str(lendata) + ' note')
    time.sleep(0.5)
    while lendata > 0:
        update.message.reply_text("Title: " + str(v.shownote()[lendata - 1][1])) # title
        time.sleep(0.5)
        update.message.reply_text(v.shownote()[lendata - 1][2]) # content
        lendata -= 1

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

def button_del_job(update: Update, context: CallbackContext) -> None:
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
    update.message.reply_text('\n 1- For take job "/getjob"'
                              '\n 2- For take detail "/get {job_id} {title or content or link}. Need two argument!"'
                              '\n 3- For delete job /deljob "its delete full job on database'
                              '\n 4- For add rss /addrss {rss link here}'
                              '\n 5- For dell rss /delrss'
                              '\n 6- For read log /getlog {how much record}'
                              '\n 7- For add proposal note /addnote {text here}'
                              '\n 8- For show proposal note /shownote'
                              '\n 9- İf direct write job number, show job title and job content')

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    v.write_log("Error","Wrong get code")
    update.message.reply_text("Wrong! if you want help, you can write /help")


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
    dp.add_handler(CommandHandler("shownote", shownote))
    dp.add_handler(CommandHandler("addnote", addnote))
    dp.add_handler(CommandHandler("delrss", del_rss))
    updater.dispatcher.add_handler(CallbackQueryHandler(button_del_job))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, direct_job))
    dp.add_handler(CommandHandler("help", help))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()

