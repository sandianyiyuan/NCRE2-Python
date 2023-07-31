sumtime = 0
percls = []
ts = {}
with open('out.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n').split(',')
        sumtime += eval(line[1])
        ts[line[0]] = line[2]

print('the total execute time is ', sumtime)

tns = list(ts.items())
tns.sort(key=lambda x: x[1], reverse=True)
for i in range(3):
    print('the top {} percentage time is {}, spent in "{}" operation'.format(
        i, tns[i][1], tns[i][0]))
