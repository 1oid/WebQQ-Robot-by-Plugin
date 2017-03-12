# coding:utf-8
import sys,os
def load_Plugins():
    func = lambda x:(True,False)[x[:8]=='__init__' or x[-4:]=='.pyc' and not x[-3:]=='.py']
    return filter(func,os.listdir('./plugins'))

def load_return(command,plugin):
    import_plugin = __import__(plugin.split(".py")[0])
    p = getattr(import_plugin,'Plugin')(command)
    response = p._cmd()
    if response:
        return {"status":1,"result":response}
    else:
        return {"status":0,"result":response}