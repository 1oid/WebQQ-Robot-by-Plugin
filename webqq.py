# coding:utf-8
from webQQfunction import *
import requests
from startConf import *
cookies2 = COOKIE_INI()
data = POLL_DATA_INI()
headers = HEADERS_INI()


import threading
threads = []

for i in range(5):
    threads.append(threading.Thread(target=get_polls,args=[data,headers,cookies2,]))
for t in threads:
    t.start()

