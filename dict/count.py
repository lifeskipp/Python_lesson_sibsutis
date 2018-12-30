#это решение по выходным данным
dict = {}
for count in input().split():
    dict[count] = dict.get(count, 0) + 1
print(dict)

#а это по условию задачи

'''
dict = {}
for count in input().split():
    dict[count] = dict.get(count, 0) + 1
    print(dict[count] - 1, end=' ')
'''

