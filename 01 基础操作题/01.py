import jieba
txt = input("请输入一段中文文本:")
ls = jieba.lcut(txt)
print(ls)
print("{:.1f}".format(len(txt)/len(ls)))
