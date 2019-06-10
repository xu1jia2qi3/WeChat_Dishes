import itchat
from itchat.content import *
from plugins.XiaChuFang import XiaChuFang
import requests
import os


def download_img(url, file_path):
    res = requests.get(url, allow_redirects=True)
    with open(file_path, 'wb') as output_file:
        output_file.write(res.content)


provider = XiaChuFang(3)


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg)
    if '吃' in msg['Text'] and msg.isAt:
        for index, menu in enumerate(provider.get_menu()):
            file_path = 'assets/tmp.jpg'
            download_img(menu['img'], file_path)
            msg.user.send('title: ' + menu['title'])
            msg.user.send_image(file_path)
            msg.user.send('url: ' + menu['url'])
            os.remove(file_path)


itchat.auto_login(True)
itchat.run(True)
