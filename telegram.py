import config
import requests
from vt import *


class send():
    def __init__(self):
        self.token = config.bot_token
        self.id = config.chat_id
        self.v = vt()

    def send_message(self,message):
        link = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(self.token,self.id,message)
        requests.post(link)

