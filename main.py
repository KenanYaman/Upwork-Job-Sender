from apscheduler.schedulers.background import BlockingScheduler
from upwork import *
import config


scheduler = BlockingScheduler()
scheduler.add_job(Upwork().take_job, 'interval', hours=config.time_hour, minutes=config.time_minute)



while True:
    print("""
        1- Run Application
        2- Add Rss
        """)
    take = int(input("Seçim yapın! : "))

    if take == 1:
        if vt().check_rss() == True:
            vt().Create_table()
            vt().write_log('İnfo', 'App runing')
            print("App Runing...")
            scheduler.start()
        else:
            print('Not added rss, please first add rss')
            vt().write_log('Error', 'App not start, because not have rss link')
    elif take == 2:
        rss = input('How many you want add rss ?: (press q for quit) -->')
        if rss == 'q':
            quit()
        else:
            count = 0
            while count < int(rss):
                link = input('Add Rss Link: --> ')
                vt().add_rss(link)
                vt().write_log('info', 'Rss Added')
                count += 1
            vt().write_log('info',rss + ' piece rss added')



