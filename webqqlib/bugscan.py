# coding:utf-8
import requests,json

class Bugscan:
    '''
    Bugscan 使用接口
    Cookie : 自行替换
    Time: 2017-0204
    Author: Loid
    '''
    def __init__(self):
        self.request_Strings = ''
        self.htmlHeader = htmlHeader = '''

<html>
<title>Test</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<body>
    '''

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8"}
        self.cookies = {
            "Cookie": 'user_id=7715; userface="http%3A//q.qlogo.cn/qqapp/101191243/F8960B0A62B24B1506DCE2933698C393/100"; sessionid=xrgos6k9f8jh48ylqg34czj7kqh63cbo; gsid=4e403284a5e8bfbc142acc8c666f8987a4ad509e5a5370da01c02a05b70443176df94b8ef910230c1761d883c6c135f944c21d; nickname=%E6%B6%88_%E6%9E%81_%E6%82%A3_%E8%80%85; csrftoken=KIGkvlV0LO5XxNK9xsWBN2n6DFJdCSxYL1L8WIOqYTHCE3e4UqW7TTWGdfhnicU2; _ga=GA1.2.1914929831.1486117300; TZ=28800'}

    # 用于获取扫描结果信息
    def getNamefromId(self, id, ids):
        for i in ids:
            if id == i.keys()[0]:
                return i.values()[0]
        return ""

    # 添加扫描
    def bugscanAdd(self,url):
        if url[:4]+url[-1] != "http/":
            print "http://%s/"%url
            data = {"method":"TaskDispatch","params":[{"single":True,"target":"http://%s/"%url,"targets":"","scanport":False,"subdomain":False,"maxtask":7000,"speed":6,"timeout":24,"useragent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; .NET CLR 2.0.50727)","disallow":"logout;log_out;/admin;/manage;/phpmyadmin","disallow_enable":False,"cookie":"","anyone":True,"user_dict":"","pass_dict":"","modules":[2,3,4,5,6,1,7,8,9],"nodes":[60727]}]}
            req = requests.post("https://old.bugscan.net/rest",
                                data=json.dumps(data),cookies=self.cookies,headers=self.headers)
            result = req.json().get("result")
            if len(result) != 0:
                return str(result[0])
        return u"null,请检查您的url有效性 正确例子:xxx.com,或者已经开始扫描。"

    # 查询扫描状态
    def bugscanReset(self,params):
        data = {"method": "GetTaskLogs", "params": [int(params)]}
        req = requests.post("https://old.bugscan.net/rest",
                            data=json.dumps(data),cookies=self.cookies,headers=self.headers)
        jsons = req.json()["result"]["logs"]
        logs = map(lambda x:{x["body"]:x["plugin_id"]},jsons)
        func_id = lambda x:{x.values()[0]:x.values()[1]}
        ids = map(func_id,req.json()["result"]["plugins"])
        func2 = lambda x:{x.keys()[0]:self.getNamefromId(x.values()[0],ids)}
        scan_Result = map(func2,logs)
        for i in scan_Result:
            self.request_Strings = self.request_Strings+"<br><br>"+str(i.values()[0].encode("utf-8"))+"  ==>  "+str(i.keys()[0].encode("utf-8"))

        req2 = requests.post("http://45.78.10.59/bugscan.php",
                             data={"data":self.htmlHeader+self.request_Strings,"paramsid":params})
        self.request_Strings = ''
        progress = req.json()["result"].get("task")["progress"]
        return "http://45.78.10.59/%s.html"%params,progress

    ### Manager:Contral:
    # 查询所有已扫描的目标网址 id 扫描进程
    # 仅限管理员操作
    def show_task_list(self):
        data = {"method":"GetTaskList","params":[0,12,-1,-1,""]}
        req = requests.post("https://old.bugscan.net/rest",
                            data=json.dumps(data),headers=self.headers,cookies=self.cookies)
        targets = req.json()['result']['tasks']
        func = lambda x:"%s : %s : %s"%(x.get("target"),x.get("id"),x.get("progress"))
        return '\n'.join(map(func,targets)[:5])

    def stop_task(self,parmas):
        data = {"method":"StopTask","params":[[int(parmas)]]}
        req = requests.post("https://old.bugscan.net/rest",data=json.dumps(data),headers=self.headers,cookies=self.cookies)
        if req.json().get("result") == 1:
            return "Stoped %s"%parmas
        return "Stop Failed!"
