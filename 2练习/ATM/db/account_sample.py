# -*- coding:utf-8 -*-
import json
import random
import string
from hashlib import md5

salt = ''.join(random.sample(string.digits + string.ascii_letters + string.punctuation, 8))
md5_value = md5()
md5_value.update(b'123'+salt.encode('utf-8'))

account_dic = {
    'id': 999,
    'password': md5_value.hexdigest(),
    'salt': salt,
    'balance': 15000,  # 账户余额
    'credit': 15000,  # 信用额度
    'enroll_date': '2016-01-01',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0  # 0 = normal, 1 = locked, 2 = disabled
}

print(json.dumps(account_dic))
# json.dump(account_dic, open('./accounts/999.json', 'w', encoding='utf-8'))