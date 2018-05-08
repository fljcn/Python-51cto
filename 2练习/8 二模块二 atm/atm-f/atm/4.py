
account = int(input('account id:'))
import os,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = "%s/db/account" % BASE_DIR

print('BASE_DIR:', BASE_DIR)
print('DB_PATH:', DB_PATH)


account_file = os.path.join(DB_PATH, "%s.json" % account)
aaa = os.path.isfile(account_file)
f=open(account_file)
data=json.load(f)
print(data)
print('aaa:',aaa)

print('account_file:', account_file)



# if os.path.isfile(account_file):
#     f = open(account_file)
#     data = json.load(f)  # json dict
#     f.close()
#     return {'status': 0, 'data': data}