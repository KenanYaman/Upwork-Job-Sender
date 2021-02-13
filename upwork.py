from sender import *
import feedparser
import re
from apscheduler.schedulers.background import BlockingScheduler


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
                if self.v.filter(link):
                    pass
                else:
                    self.v.into_data(title,content,published,link)
                    count += 1
        if count > 0:
            self.v.write_log('Add Job', str(count) + ' Job added' )


scheduler = BlockingScheduler()
scheduler.add_job(Upwork().take_job, 'interval', hours=config.time_hour, minutes=config.time_minute)
scheduler.start()
