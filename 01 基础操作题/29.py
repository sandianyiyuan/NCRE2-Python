ns = input("请输入一串数据：")
dnum,dchr = 0, 0
for i in ns:
    if i.isnumeric():
        inu
        dnum += 1
    elif i.isalpha():
        dchr += 1
    else:
        pass
print('数字个数：{}，字母个数：{}'.format(dnum,dchr))
