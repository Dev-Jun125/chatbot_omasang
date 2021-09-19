import schedule
import information_scraper
import time


def cafeteria_update():
    information_scraper.cafeteria_info()

def notice_update():
    information_scraper.general_info()
    information_scraper.collage_info()

def timer():
    # tm = time.time()
    # localtime = time.localtime()
    # hourminute = time.strftime('%H : %M', localtime(tm))
    print(time.strftime('\rwaiting for update... %X', time.localtime(time.time())), end='')

# schedule.every(1).second.do(timer)
schedule.every().monday.at("10:30").do(cafeteria_update)
schedule.every(3).hours.do(notice_update)

while True:
    schedule.run_pending()
    # time.sleep(1)

# ex))
# schedule.every(30).minutes.do(printhello) #30분마다 실행
# schedule.every().monday.at("00:10").do(printhello) #월요일 00:10분에 실행
# schedule.every().day.at("10:30").do(job) #매일 10시30분에 