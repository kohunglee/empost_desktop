# 发布笔记的窗口

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from cgitb import handler
import webbrowser
import ipaddress
from pickle import TRUE
import tkinter as tk
import tkinter.font as tf
import tkinter.messagebox as tm
import em_module as em
import em_req


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
            print(len(noteText))
            if len(noteText) <= 1 :
                tm.showinfo("", "请填写内容！")
                return
            res = em_req.req("note_post", em.note(noteText))
            topMsg.set(res)
        except :
            tm.showinfo("", "无法发送！网络问题或程序配置错误！")
            return

        if eval(res)["msg"] == "ok":
            tm.showinfo("", "发表成功!")
        else:
            tm.showinfo("", "发送失败！请检查配置信息！")

        topMsg.set(res)
        return
    
    # 创造配置窗口
    def create_setting(event):
        top = tk.Toplevel()
        top.title("emPost 配置")

        width = 300
        height = 200
        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2 - 100)

        top.geometry(size_geo)

        msg = tk.Label(top, text="网址：c.biancheng.net",bg='#9BCD9B',font=('宋体',15))

        msg.pack() 

    # 笨办法、变红、变黑
    def change_color1(event):
        lSetting.config(fg ="red")
        return

    def change_color2(event):
        lSetting.config(fg ="black")
        return

    # 打开网址
    def open_url(event):
        webbrowser.open(em.url)

    # 动态文字
    topMsg = tk.StringVar()
    topMsg.set(em.url)
    labelMsg = tk.Label(window, fg = "#806520", textvariable=topMsg)
    labelMsg.bind("<Button-1>",open_url)
    labelMsg.pack(pady = "7px")

    # 文本输入框属性
    text = tk.Text(window, width=50, font = tf.Font(size=16), fg ="#5a5c69", height=10,
                   padx = 5,pady = 5, undo=True, autoseparators=False,borderwidth = "0px")
    text.pack(padx = "10px",fill = tk.BOTH,expand=tk.TRUE)
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
    
    tk.Label(frame_left,text='发文').grid(row = 0, column =1)
    tk.Label(frame_left,text='读文').grid(row = 0, column =3)
    frame_left.pack()

    window.mainloop()
    return

note_view();