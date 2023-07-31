img = [0.244, 0.832, 0.903, 0.145, 0.26, 0.452]
filter = [0.1, 0.8, 0.1]
res = []
for i in range(5):
    k = 0
    for j in range(3):
        k += filter[j]*img[i+j]
        print('k={:<10.3f},filter[{}]={:<10.3f},img[{}+{}]={:<10.3f}'.format(
            k, j, filter[j], i, j, img[i+j]))
    res.append(k)
for r in res:
    print('{:<10.3f}'.format(r), end='')
