s = input()
list = s.split()
count = 0
for i in range(1, len(list)-1):
    if list[i-1] < list[i] > list[i + 1]:
       count += 1
print(count)
