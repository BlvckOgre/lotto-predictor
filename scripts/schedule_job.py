
import schedule
import time
from fetch_latest_draw import fetch_latest

schedule.every().wednesday.at("21:00").do(fetch_latest)
schedule.every().saturday.at("21:00").do(fetch_latest)

while True:
    schedule.run_pending()
    time.sleep(60)
