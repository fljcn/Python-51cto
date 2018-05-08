#!/usr/bin/env python
# _*_coding:utf-8 _*_
# __author__ = Feng

import json,time,os
from conf import settings

def load_account_data(account):
    """根据account id找到对应的账户文件，并加载"""

    account_file = os.path.join(settings.DB_PATH,"%s.json" % account)
    if os.path.isfile(account_file):
        f = open(account_file)
        data = json.load(f)  #json dict
        f.close()
        return {'status':0,'data':data}
    else:
        return {'status':-1,'error':"account file does not exist."}


def save_db(account_data):