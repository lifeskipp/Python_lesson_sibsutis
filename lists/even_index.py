s = input()
list = s.split()
for i in range(len(list)):
    if i % 2 == 0:
        print(list[i], end=' ')