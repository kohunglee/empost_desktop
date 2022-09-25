# 运行库
 
import hashlib
import time
import os
import json

apikey = ""
url    = ""
version= ""

# ------------------- 

# 读取文件
def readfile(url):
    txt = ''
    try:
        f = open(url, encoding = "utf-8")
        txt = f.read()
    except:
        return 'file unexist'
    f.close()
    return txt

# 验证文件是否存在
def existfile(url):
    try:
        f = open(url, encoding = "utf-8")
    except:
        return 'false'
    f.close()
    return 'true'

# 向文件里写入内容
def written(url,text):
    if existfile(url) == 'false':
        return 'error'
    try:
        f = open(url,"w+",encoding = "utf-8")
        f.write(text)
    except:
        return 'error'
    f.close
    return 'ok'

# 新建文件、向文件里写入内容
def makefile(url,text):
    if existfile(url) == 'true':
        return 'error'
    try:
        f = open(url,"w+",encoding = "utf-8")
        f.write(text)
    except:
        return 'error'
    f.close
    return 'ok'


makefile(os.getcwd() + "/ab.txt","hello")

# ------------------- 

# 获取配置
def reConfig():
    # configFile = open("config.json", encoding = "utf-8")
    # txt = configFile.read()
    # configFile.close()

    txt = '{"apikey":"","url":"https://www.ccgxk.com","version":"1.0.0"}';
    configJson = eval(txt)

    global apikey,url,version
    apikey = configJson["apikey"]
    url    = configJson["url"]
    version= configJson["version"]

    version= os.getcwd()

reConfig()

# 获取时间
def unix_time():
    return str(int(time.time()*1000))

# 生成笔记数据
def note(text):
    getTimeNow = unix_time()
    return {
            "req_time":getTimeNow,
            "req_sign":make_sign(getTimeNow),
            "t":text
        }

# 生成签名 (根据 api 规则，MD5 加盐 “unix时间戳” + “api秘钥”)
def make_sign(time):
    signSource = time + apikey 
    signSource = hashlib.md5(bytes(signSource,encoding = 'utf-8'))
    return signSource.hexdigest()


    