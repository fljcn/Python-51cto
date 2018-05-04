import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}
print(DATABASE)
print(DATABASE['path'])
print(DATABASE['name'])
print(DATABASE['path'],DATABASE['name'])
db_path='%s/%s' % (DATABASE['path'],DATABASE['name'])
print(db_path)
print('sql_f:', sql)