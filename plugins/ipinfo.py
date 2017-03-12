# coding:utf-8
# 开发插件实例

# 导入所需要的模块
import requests
class Plugin:
    '''
    这是一个ip定位插件
    '''
    # 初始化
    def __init__(self,command):
        self.command = command

    def function(self,ip):
        req = requests.get("http://1.webscanner.applinzi.com/ipinfo?ip=%s" % ip).content
        if req == "0":
            return "No Information!"
        return req

    # 判断用户发送的指令
    # 发送过来的指令  ip:127.0.0.1
    def _cmd(self):
        if self.command[:3] == 'ip:':
            # 分割提取ip
            ip = self.command.split(":")[1]
            return self.function(ip)
