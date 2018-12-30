a = int(input())
if a == 0:
    print(0)
else:
    prev, next = 0, 1
    number = 1
    while next <= a:
        if next == a:
            print(number)
            break
        prev, next = next, prev + next
        number += 1
    else:
        print('False')
