# data_file = open('staff_table.txt', 'r+', encoding='utf-8')
# data = data_file.readlines()
# data_file.close()
# print('data:', data)
# data_list = []
# for i in data:
#     data_list.append(str(i).strip().split(','))
#     # data_list.append(str.strip(i).split(','))
# print('data_list:', data_list)


with open('staff_table.txt', 'r+',encoding='utf-8') as staff_file:
    data = staff_file.readlines()
    data_list = []
    for i in data:
        data_list.append(str(i).strip().split(','))
    print('data_list:',data_list)
