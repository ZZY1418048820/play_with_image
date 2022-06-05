# -*- coding: utf-8 -*-
"""
@Time : 04/06/2022 10:30 PM
@Auth : Zhang Zhuoyi
@File : BM25.py.py
@IDE  : PyCharm
"""
import numpy
from PIL import Image
import tkinter
from tkinter import filedialog, messagebox

path = ''
output = ''
root = tkinter.Tk()


def selectFile():
    global path
    global output
    text.delete('1.0', 'end')
    path = filedialog.askopenfilename()
    if path and path != "":
        print("文件路径: {}".format(path))
        text.insert('1.0', "文件路径: {}\n".format(path))
    output = path.replace(path.split("/")[-1].split(".")[-1], "txt")
    if path:
        print("输出路径: {}".format(output))
        text.insert('2.0', "输出路径: {}\n".format(output))
    label["text"] = path.split("/")[-1]


def process():
    global path
    global output
    info = entry.get().split()
    for key in info:
        if key.isdigit():
            messagebox.showerror("哔哔哔", "数字不可以嗷兄弟")
            return
        if key == "":
            info.remove(key)
    if len(info) < 2:
        messagebox.showerror("哔哔哔", "最起码得一个字以上吧老铁")
        return
    text.insert("3.0", "处理着呢别急! {}\n".format(path))
    img = Image.open(path)
    img = img.resize((300, 300), Image.Resampling.LANCZOS)
    image = img.convert('L')
    image = numpy.array(image)
    image_max = image.max()
    image_min = image.min()
    alpha = (image_max - image_min) / len(info)
    with open(output, 'w') as f:
        for i in range(len(image)):
            for j in range(len(image[0])):
                res = int((image[i][j] - image_min) / alpha)
                f.write(info[len(info) - 1 - (len(info) - res)])
                f.write(" ")
            f.write("\n")
    text.insert("4.0", "这不就好了~ {}\n".format(output))


if __name__ == '__main__':
    root.geometry('500x350')
    title = tkinter.Label(root, text="先看左 再输右")
    title.pack(pady=10)
    frame_m = tkinter.Frame(root)
    frame_t = tkinter.Frame(frame_m)
    frame_l = tkinter.Frame(frame_t)
    frame_r = tkinter.Frame(frame_t)
    frame_b = tkinter.Frame(frame_m)
    frame_l.pack(side='left', padx=15)
    frame_r.pack(side='right', padx=15)
    frame_t.pack(side='top')
    frame_b.pack(side='bottom', pady=15)
    root.title("就是说咱可以用名字画图你信不")
    prompt = tkinter.Label(frame_l, text="绘图所用字符：\n笔画多的给我放前面！\n（字多些效果更佳哈）\n如: '毅 卓 张 帅 点 亿'",
                           justify=tkinter.LEFT)
    prompt.pack()
    entry = tkinter.Entry(frame_r, bd=6)
    entry.pack()
    label = tkinter.Label(frame_r, text="快选个图像！")
    label.pack()
    select = tkinter.Button(frame_b, text="先点这里（选择文件）", command=selectFile)
    select.pack()
    start = tkinter.Button(frame_b, text="再点这里（开始转换）", command=process)
    start.pack()
    frame_m.pack(pady=30)
    text = tkinter.Text(frame_b, height=5, width=50)
    text.pack(pady=15)
    root.mainloop()


