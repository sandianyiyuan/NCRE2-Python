import jieba

s = input("请输入一段中文文本，句子之间以逗号或句号分隔：")
slist = jieba.lcut(s)
m = 0

for i in slist:
    if i in "，。":
        continue
    print(i, end='/')
    m += 1

print("\n中文词语数是：{}\n".format(m))

s = ''
for i in slist:
    if i in "，。":
        print('{:^20}'.format(s))
        s = ''
        continue
    s += i
