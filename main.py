"""Python Website Blockr"""
#Block sites for a specific time period

import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.wallpapersden.com", "wallpapersden.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
    
    else:
        print("None working hours...")

    #sleep for 5 sec
    time.sleep(5)