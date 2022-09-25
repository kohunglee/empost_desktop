# 发送 GET/POST 请求 
 
import requests
import em_module as em

def req(type, param):
    if type == "note_post": # 发表笔记
        url     = em.url + "?rest-api=" + type
        payload = param
        headers = {'User-Agent': 'emPost_desktop/1.0.0 (https://www.ccgxk.com)'}

        # print("发送的数据" + str(payload))

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text

    elif type == "1":
        
        pass
        return

    elif type == "2":

        pass
        return

    elif type == "3":

        pass
        return

    else:
        return


def analyse(jsonStr):
    json = eval(jsonStr)
    return