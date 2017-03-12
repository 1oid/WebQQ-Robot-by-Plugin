# coding:utf-8
import requests
'''
使用接口查询ip
'''

def get_information(ip):
    req = requests.get("http://1.webscanner.applinzi.com/ipinfo?ip=%s"%ip).content
    if req == "0":
        return u"No Information!"
    return req