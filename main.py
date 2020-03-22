"""Python Website Blockr"""
#Block sites for a specific time period

import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.wallpapersden.com", "wallpapersden.com"]

while True:
    print(1)
    #sleep for 5 sec
    time.sleep(5)