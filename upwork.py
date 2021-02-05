from telegram import *
import feedparser
import re
import time



class Upwork():
    def __init__(self):
        self.v = vt()

    def take_job(self):
        count = 0
        for i in self.v.take_data_all('rss'):
            rss = feedparser.parse(i[1])
            feed_entries = rss.entries
            for data in feed_entries:
                title = data.title
                published = data.published
                contentD = data.summary
                content = re.sub("<[^<]+?>", " ", contentD)
                link = data.link
                # print(title,published,content,link)
                if self.v.filter(link):
                    pass
                else:
                    self.v.into_data(title,content,published,link)
                    count += 1
        if count > 0:
            self.v.write_log('Add Job', str(count) + ' Job added' )

        time.sleep(120)

        a = len(vt().fetch_data())
        self.v.write_log('Send Job', str(a) + ' Job sended')
        while a > 0:
            b = vt().fetch_data()[a - 1][0]
            send().send_message(vt().fetch_data()[a - 1][1])  # title
            # s.send_message(v.fetch_data()[a -1][2])#content
            send().send_message(vt().fetch_data()[a - 1][4])  # link
            a -= 1
            vt().change(b)


