a = [int(s) for s in input().split()]
for i in range(len(a)-1):
    if i % 2 == 0:
        a[i], a[i + 1] = a[i + 1], a[i]
print(' '.join([str(i) for i in a]))
