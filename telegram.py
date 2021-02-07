import config
import requests
from vt import *


class send():
    def __init__(self):
        self.token = config.bot_token
        self.id = config.chat_id
        self.v = vt()

    def send_message(self,*args):
        link = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(self.token,self.id,str(args[0]) +" - "+ str(args[1]) +" ------------ " + str(args[2]) + " ------------ " + str(args[3]))
        requests.post(link)

