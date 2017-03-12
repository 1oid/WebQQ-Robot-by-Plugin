# coding:utf-8
from startConf import *
import requests,urllib,sys
from lib.functions import *
sys.path.append("plugins")
plugins = load_Plugins()


# webqq抓取的cookies
cookies2 = COOKIE_INI()
# webqq poll2的参数
data = POLL_DATA_INI()
# headers
headers = HEADERS_INI()
# bugscan扫描次数限制
# bugscan_id = BUGSCAN_INI()
# webqq 抓取的管理员id
manager_id = MANAGER_ID()
# 发送群消息的参数
send_to_params = SEND_TO_PARAMS()

# 发送消息给群的接口
def send_to_group(group_uin,content="Hello,World"):
    # 发送内容编码为utf8
    # content = unicode(content).encode("utf-8")
    data2 = send_to_params%(int(group_uin),content)
    req = requests.post("https://d1.web2.qq.com/channel/send_qun_msg2",
                        data=data2,headers=headers,cookies=cookies2)
    #  返回 code
    # : 100100 --> 正常
    if req.json().get("retcode") == 100100:
        print "send %s ok! " % req.status_code

# 发送信息给私人的接口
def send_to_self(group_uin,content="Hello,World"):
    data2 = send_to_params%(group_uin,content)
    req = requests.post("https://d1.web2.qq.com/channel/send_buddy_msg2",
                        data=data2,headers=headers,cookies=cookies2)

    #  返回 code
    # : 100100 --> 正常
    if req.json().get("retcode") == 100100:
        print "send %s ok! " % req.status_code

# 群的
# 接受字符串后的判断
def funcGet_group(group_uin,content):
    if PASS_COMMAND(content):
        for plugin in plugins:
            returm_msg = load_return(content,plugin)
            if returm_msg.get("status") == 1:
                send_to_group(group_uin,returm_msg.get('result'))
            else:
                continue

# 发给自己的 消息处理函数
def funcGet_self(group_uin,content):
    if group_uin == manager_id[0] or group_uin == manager_id[1]:
        pass

def get_polls(data,headers,cookies):
    while True:
        try:
            req = requests.post('https://d1.web2.qq.com/channel/poll2',
                                data=data,headers=headers,cookies=cookies,timeout=20)
            if req.status_code == 200:
                msg_type = req.json()["result"][0]["poll_type"]
                group_type = req.json()["result"][0]["value"]
                group_uin = group_type["from_uin"]
                content = group_type["content"]
                print content

                # 这里对群消息和私人消息区分
                #
                if msg_type == "group_message":

                    # 判断参数 (因为电脑qq可能穿过来的参数是不一样的)
                    if len(content) == 2 :
                        content = content[1]
                        funcGet_group(group_uin,content)
                    elif len(content) == 3 :
                        funcGet_group(group_uin,content[1]+content[2])

                elif msg_type == "message":
                    if len(content) == 2:
                        funcGet_self(group_uin,content[1])
        # 一堆报错处理
        except requests.exceptions.ReadTimeout,e:
            print "RESET"
            continue
        except KeyError,e:
            send_to_group(int(group_uin),content="")
            continue
        except TypeError,e:
            print e
            send_to_group(int(group_uin), content=urllib.quote("Type Error!"))
        except ValueError,e:
            print e
            send_to_group(int(group_uin), content=urllib.quote(u"数据传输错误,请联系管理员帮忙查看/修复.".encode("utf-8")))
            continue
        except IndexError,e:
            print e
            send_to_group(int(group_uin), content=urllib.quote("No msg!"))
