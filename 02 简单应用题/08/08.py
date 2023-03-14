import os
path = os.path.dirname(__file__)
f = open(path+"/vote.txt")
names = f.readlines()
f.close()
n = 0
for name in names:
    num = len(name.split())
    if num == 1:
        n += 1
print("有效票{}张".format(n))

D = {}
for name in names:
    if len(name.split()) == 1:
        D[name[:-1]] = D.get(name[:-1], 0) + 1
l = list(D.items())
l.sort(key=lambda s: s[1], reverse=True)
name = l[0][0]
score = l[0][1]
print("最具人气明星为:{},票数为：{}".format(name, score))
