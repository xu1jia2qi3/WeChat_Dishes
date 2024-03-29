# 用 Python + itchat 写一个爬虫脚本 自动回复菜谱

## 项目介绍：

开发环境：Python >= 3.5

### 项目地址：
Github: [https://github.com/xu1jia2qi3/WeChat_Dishes.git]

### 使用库
- [itchat](https://itchat.readthedocs.io/zh/latest/)- 微信个人号接口
- [requests](http://docs.python-requests.org/en/master/) -网络请求库
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#) - 解析网页

### 功能
自动回复网上爬取菜单

### 数据来源
- 菜单来自下厨房(https://www.xiachufang.com/)  
测试版只爬取了一家， 之后可以更新更多

### 效果展示
<img src="demo/demo1.png" width="30%" height="30%">

## 代码说明

### 目录结构
- server.py : 运行服务器代码， 设置关键词和菜单数量
- assets ： 缓存菜单图片， 方便微信发送
- plugins: <br />
    -DummyProvider.py: 测试 代码假菜单 <br />
    -MenuProvider.py ：初始class，方便之后添加其他菜单 <br />
    -XiaChuFang.py   : 爬取下厨房 每周精选菜单 <br />

## 项目配置

### 安装依赖

- pip install beautifulsoup4
- pip install itchat 
- pip install requests

## 项目运行

建议使用微信小号。怕有封号风险

### 1.直接运行
```
python server.py, 微信扫码登录，目前仅支持群聊天里，@本人 外加关键词 "吃" 
如需修改 请修改server.py中关键词，及参考itchat api
```


  
