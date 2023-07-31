import random as r

r.seed(0)
persons = ['Aele', 'Bob', 'lala', 'baicai']
flag = 3
while flag > 0:
    flag -= 1
    name = input("请输入一个名字：")
    if name in persons:
        num = r.randint(1000, 9999)
        print('{} {}'.format(name, num))
    elif name == 'q':
        break
    elif name not in persons:
        print('对不起，您输入的名字不存在。')
