#это решение по выходным данным
diction = {}
for count in input().split():
    diction[count] = diction.get(count, 0) + 1
print(diction)

#а это по условию задачи

'''
diction = {}
for count in input().split():
    diction[count] = diction.get(count, 0) + 1
    print(diction[count] - 1, end=' ')
'''

