import itchat
import requests
import os
from itchat.content import *
from plugins.XiaChuFang import XiaChuFang


def download_img(url, file_path):
    res = requests.get(url, allow_redirects=True)
    with open(file_path, 'wb') as output_file:
        output_file.write(res.content)


# set the recipe number you want to get
provider = XiaChuFang(3)


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    # set key word to active auto reply, also user much be @ in wechat
    if '吃' in msg['Text'] and msg.isAt:
        for menu in provider.get_menu():
            file_path = 'assets/tmp.jpg'
            download_img(menu['img'], file_path)
            msg.user.send('*' * 20)
            msg.user.send(menu['title'])
            msg.user.send_image(file_path)
            msg.user.send(menu['url'])
            os.remove(file_path)


itchat.auto_login(True)
itchat.run(True)
