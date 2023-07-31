import os

path = os.path.dirname(__file__)
f = open(path+'/data18.txt', 'r', encoding='utf-8')

school = []
country = []
for line in f:
    lines = line.strip('\n').split(",")
    if lines != ['']:
        school.append(lines[1:3])  # 构建学校列表
        country.append(lines[-1])  # 构建国家列表

country = list(set(country))  # 列表去重复

unis = []
for i in country:
    n = 0
    schools = []
    result = []
    for k in school:
        if k[1] == i:
            n += 1
            schools.append(k[0])
    result = [i, n, schools]
    unis.append(result)

for d in unis:
    print('{:>4}: {:>4} : {}'.format(d[0], d[1], ' '.join(d[2])))

f.close()
