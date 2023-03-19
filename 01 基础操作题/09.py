n = eval(input("请输入数量："))
if n == 1:
    cost = n * 160
elif n <= 4:
    cost = n * 160 * 0.9
elif n <= 9:
    cost = n * 160 * 0.8
else:
    cost = n * 160 * 0.7
print("总额为:", cost)
