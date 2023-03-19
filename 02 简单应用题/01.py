txt = input("请输入类型序列")

tem = txt.split()
d = {}

for i in range(len(tem)):
    d[tem[i]] = d.get(tem[i], 0)+1

ls = list(d.items())  # 将字典转换成list。([('综合', 4), ('理工', 2), ('师范', 1)])

ls.sort(key=lambda x: x[1], reverse=True)   # 匿名表达式，按列表的第一个参数进行排序

for k in ls:
    print("{}:{}".format(k[0], k[1]))
