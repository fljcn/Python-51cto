import re
def judge_num(num):
    # 判断 int float
    str_num = re.sub('\.', '', num, count=1)
    print(str_num.isdigit())
    print(num.isdigit())

    if str_num.isdigit():
        return float(num)

while True:
    money = input('withdraw_money(q表示退出)>>>:').strip()
    if not money:
        continue
    if money == 'q':
        break
    float_money = judge_num(money)


