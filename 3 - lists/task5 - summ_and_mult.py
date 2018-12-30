a = [int(s) for s in input().split()]
summ = 0
mult = 1
for i in range(len(a)):
    summ += a[i]
    mult *= a[i]
print(summ, ' ', mult)
