a = [3, 6, 9]
b = eval(input())  # 例如：[1,2,3]
s = 0
for i in range(3):
    s += a[i]*b[i]
print(s)
