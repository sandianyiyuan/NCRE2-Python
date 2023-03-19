n = eval(input("请输入一个数字:"))
print("{:+^11}".format(chr(n-1)+chr(n)+chr(n+1)))

n = eval(input("请输入正整数:"))
print("{:->20,}".format(n))
