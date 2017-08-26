# -*- coding: utf-8 -*-

import pymongo
from settings import *

class MongodbHandeler(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[MONGO_DB]  # 获得数据库的句柄
        self.coll = self.db[MONGO_COLL]  # 获得collection的句柄

    def process_item(self, item):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写