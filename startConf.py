# coding:utf-8
# 主要配置文件

# webqq Cookie
def COOKIE_INI():
    COOKIE = "your webqq cookie"
    return {"Cookie":COOKIE}

#这里不用替换太多 替换ptwebqq就可以了
def POLL_DATA_INI():
    ARGV = '{"ptwebqq":"your webqq ptwebqq","clientid":53999199,"psessionid":"8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857","key":""}'
    DATA = 'r=%s'%ARGV
    return  DATA

def HEADERS_INI():
    return {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0","Content-Type":"application/x-www-form-urlencoded","Referer":"https://d1.web2.qq.com/cfproxy.html?v=20151105001&callback=1"}

def BUGSCAN_INI():
    return 2

# 定义管理员id 可以不设置
def MANAGER_ID():
    return 878196506,803747284

def SEND_TO_PARAMS():
    return r'r={"group_uin":%s,"content":"[\"%s\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]","face":0,"clientid":53999199,"msg_id":46120001,"psessionid":"8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857"}'

# 为了不耗机器人反应时间 必须要在里面加入你的指令
def PASS_COMMAND(command):
    ALLOW_COMMANDS = ['ip','help']
    func = lambda x:(False,True)[x in command]
    return True if len(filter(func,ALLOW_COMMANDS)) >= 1 else False