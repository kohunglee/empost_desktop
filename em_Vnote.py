# 发布笔记的窗口

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ast import Delete
from cgitb import handler
import webbrowser
import ipaddress
from pickle import TRUE
import tkinter as tk
import tkinter.font as tf
import tkinter.messagebox as tm
import em_module as em
import em_req

# 配置窗口的生成
def view_setting(topMsg):
    top = tk.Toplevel()
    top.title("emPost 配置")

    width = 250
    height = 170
    screenwidth = top.winfo_screenwidth()
    screenheight = top.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2 - 100)
    top.geometry(size_geo)
    top.resizable(0,0) # 窗口不能调大小

    em.reConfig()
    apikey = em.apikey
    url = em.url
    if apikey == '':
        url = ''

    def saveInfo():
        if em.save_config(akEText.get(), urlEText.get()) == "true" :
            tm.showinfo("", "保存成功！")
            topMsg.set(em.url)
        else:
            tm.showinfo("", "保存失败！")

    msg1 = tk.Label(top, text="API 秘钥：",font=('宋体',14))
    msg1.pack(anchor="w",padx="30px")

    akE = tk.Entry(top)
    akEText = tk.StringVar()
    akE["textvariable"] = akEText
    akE.pack(padx="10px", pady="5px")
    akE.focus()
    akE.insert(0,apikey)

    msg2 = tk.Label(top, text="站点（加 https:// ）：",font=('宋体',14))
    msg2.pack(anchor="w",padx="30px")

    urlE = tk.Entry(top)
    urlEText = tk.StringVar()
    urlE["textvariable"] = urlEText
    urlE.pack(padx="10px", pady="5px")
    urlE.insert(0,url)

    # 按钮 
    saveButton = tk.Button(top, text="保存配置",  command=saveInfo)
    saveButton.pack(pady = "10px")

# 发文窗口的生成
def create_SendArticle(event):
    top2 = tk.Toplevel()
    top2.title("发文")

    width = 300
    height = 200
    screenwidth = top2.winfo_screenwidth()
    screenheight = top2.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2 - 100)

    top2.geometry(size_geo)

    msg = tk.Label(top2, text="下一版敬请期待！",bg='#9BCD9B',font=('宋体',15))

    msg.pack()

# 阅读界面的生成
def create_Reading(event):
    top3 = tk.Toplevel()
    top3.title("读文")

    width = 300
    height = 200
    screenwidth = top3.winfo_screenwidth()
    screenheight = top3.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2 - 100)

    top3.geometry(size_geo)

    msg = tk.Label(top3, text="下一版敬请期待！！",bg='#9BCD9B',font=('宋体',15))

    msg.pack()

# 发笔记界面的生成（也是程序主窗口）
def note_view():
    
    # 定义窗口
    window = tk.Tk()
    window.title("emPost 桌面版 - 发笔记 V" + em.version)

    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    width = 500
    height = 340
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2 - 70)
    window.geometry(size_geo)
    window.minsize(width,height) # 窗口只能调大，不能调小

    # 笔记回调函数
    def note_callback():
        try:
            noteText = text.get("1.0","end")
            # print(len(noteText))
            if len(noteText) <= 1 :
                tm.showinfo("", "请填写内容！")
                return
            res = em_req.req("note_post", em.note(noteText))
        except :
            tm.showinfo("", "无法发送！网络问题或程序配置错误！")
            return

        if eval(res)["msg"] == "ok":
            tm.showinfo("", "发表成功!")
            text.delete(0.0, tk.END)
        else:
            tm.showinfo("", "发送失败！请检查配置信息！")

        # topMsg.set(res)
        return

    # 笨办法、变红、变黑
    def change_color1(event):
        lSetting.config(fg ="red")
        return

    def change_color2(event):
        lSetting.config(fg ="black")
        return

    def change_color3(event):
        lSendArticle.config(fg ="red")
        return

    def change_color4(event):
        lSendArticle.config(fg ="black")
        return

    def change_color5(event):
        lReading.config(fg ="red")
        return

    def change_color6(event):
        lReading.config(fg ="black")
        return

    # 打开网址
    def open_url(event):
        webbrowser.open(em.url + '/admin/twitter.php')

    # 动态文字
    topMsg = tk.StringVar()
    topMsg.set(em.url)
    labelMsg = tk.Label(window, fg = "#806520", textvariable=topMsg)
    labelMsg.bind("<Button-1>",open_url)
    labelMsg.pack(pady = "7px")

    # 点击 配置 按钮后
    def create_setting(event) :
        view_setting(topMsg)

    # 文本输入框属性
    text = tk.Text(window, width=50, font = tf.Font(size=16), fg ="#5a5c69", height=10,
                   padx = 5,pady = 5, undo=True, autoseparators=False,borderwidth = "0px")
    text.pack(padx = "10px",fill = tk.BOTH,expand=tk.TRUE)
    text.focus()
    # text.insert(tk.INSERT, 'some text...')

    # 按钮 
    button = tk.Button(window, text="笔记发表", font = tf.Font(size=18), command=note_callback)
    button.pack(pady = "10px", ipadx = "10px", ipady = "5px")

    # 底部的 link
    bLink = tk.Frame(window)
    bLink.pack()

    frame_left = tk.Frame(bLink)
    
    lSetting = tk.Label(frame_left, text='配置', fg ="black")
    lSetting.bind('<ButtonPress-1>',create_setting)
    lSetting.bind('<Enter>',change_color1)
    lSetting.bind('<Leave>',change_color2)
    lSetting.grid(row = 0, column=0)


    lSendArticle = tk.Label(frame_left, text='发文', fg ="black")
    lSendArticle.bind('<ButtonPress-1>',create_SendArticle)
    lSendArticle.bind('<Enter>',change_color3)
    lSendArticle.bind('<Leave>',change_color4)
    lSendArticle.grid(row = 0, column=1)

    lReading = tk.Label(frame_left, text='读文', fg ="black")
    lReading.bind('<ButtonPress-1>',create_Reading)
    lReading.bind('<Enter>',change_color5)
    lReading.bind('<Leave>',change_color6)
    lReading.grid(row = 0, column=2)
    
    frame_left.pack(pady="5px")

    window.mainloop()
    return

note_view();
