# coding:utf-8
import requests,re,random
'''
爬行华西乌云镜像站结果
'''

def getKeyword(keyword):
    req = requests.get("http://wy.hx99.net/search?keywords=%s&content_search_by=by_bugs"%keyword)
    urlLink = re.findall(r'<td><a href="(http://static.hx99.net/static/bugs/\S+)" target="_blank">(.+)</a></td>',req.content)
    func = lambda x:{x[0]:x[1]}
    res = map(func,urlLink)
    num = random.uniform(0, len(res))
    if len(res) == 0:
        return {"Null":"No Information!"}
    return res[int(num)]



