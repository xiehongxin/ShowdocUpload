# coding: utf-8
# @author: hongxin
# @date: 9/14/18

"""
上传markdown文件到showdoc的小工具

"""

import os
from tkinter import *
import tkinter.filedialog
from upload_markdown_module import import_article_to_showdoc

flag = None
file_path = None


def get_markdown_file_path():
    """
    选择要上传的文件, 并记忆选择的路径
    :return:
    """
    global file_path
    if file_path is None:
        filename = tkinter.filedialog.askopenfilename()
    else:
        # 记忆最近选择的路径
        file_root_path = os.path.realpath(os.path.dirname(file_path))
        # 传入最近路径
        filename = tkinter.filedialog.askopenfilename(**{"initialdir": file_root_path})
    if filename != '':
        # 显示选择的文件, 显得更友善
        file_path = filename
        file_info.config(text='您选择的文件是：' + file_path)
    else:
        file_info.config(text='您没有选择任何文件！')


def upload_markdown_file():
    """
    上传markdown文件到showdoc, 并在文本框显示是否成功
    :return:
    """
    global flag
    api_url = api_url_entry.get()
    api_key = api_key_entry.get()  # 获取文本框的值
    api_token = api_token_entry.get()
    article_dir = article_dir_entry.get()
    article_dir_sub = article_dir_sub_entry.get()
    article_path = file_path

    flag = import_article_to_showdoc(api_url, api_key, api_token, article_dir, article_dir_sub, article_path)
    if flag is not None:
        upload_info.config(text='上传成功！')
    else:
        upload_info.config(text='上传失败！')


if __name__ == '__main__':

    root = Tk()
    width = 600
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screen_width - width)/2, (screen_height - height)/2)
    print(size)
    root.geometry(size)

    # 文本控件, padx=25 表示距离左边25, row 和 column分别代表行和列
    api_url_label = Label(root, text='请输入api_url')
    api_url_label.grid(row=0, column=0, padx=25)
    # 输入框控件
    api_url_entry = Entry(root, width=40)
    api_url_entry.grid(row=0, column=1)

    # pady= 10 表示距离上面10
    api_key_label = Label(root, text='请输入api_key')
    api_key_label.grid(row=1, column=0, pady=10)
    api_key_entry = Entry(root, width=40)
    api_key_entry.grid(row=1, column=1)

    api_token_label = Label(root, text='请输入api_token')
    api_token_label.grid(row=2, column=0, pady=10)
    api_token_entry = Entry(root, width=40)
    api_token_entry.grid(row=2, column=1)

    article_dir_label = Label(root, text='请输入文章一级目录')
    article_dir_label.grid(row=3, column=0, pady=10)
    article_dir_entry = Entry(root, width=40)
    article_dir_entry.grid(row=3, column=1)

    article_dir_sub_label = Label(root, text='请输入文章二级目录')
    article_dir_sub_label.grid(row=4, column=0, pady=10)
    article_dir_sub_entry = Entry(root, width=40)
    article_dir_sub_entry.grid(row=4, column=1)

    file_select_btn = Button(root, text="选择文件", command=get_markdown_file_path)
    file_select_btn.grid(row=5, column=0, pady=10)
    file_info = Label(root, text='')
    file_info.grid(row=5, column=1)

    file_upload_btn = Button(root, text="开始上传", command=upload_markdown_file)
    file_upload_btn.grid(row=6, column=0, pady=10)
    upload_info = Label(root, text='')
    upload_info.grid(row=6, column=1)


    root.mainloop()

