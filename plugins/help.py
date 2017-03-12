# coding:utf-8

class Plugin:
    '''
    菜单插件
    '''
    def __init__(self,command):
        self.command = command
        self.usage = 'ip:127.0.0.1 | 定位ip'

    # 判断用户发送的指令
    # 发送过来的指令  help
    def _cmd(self):
        if self.command[:4] == 'help':
            return self.usage
