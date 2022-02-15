list1 = [5, 0, -4, 2]
x = 0
y = 2
z = 3
if list1[0] >= y and list1[1] != x:
    print('condition satisfied')
else:
    print('condition NOT satisfied')

if x and y and not z:
    print('first condition satisfied')
elif x or y or z:
    print('second condition satisfied')
else:
    print('neither condition satisfied')

if list1[0] < 0:
    print(list1[0], 'is the first negative number.')
elif list1[1] < 0:
    print(list1[1], 'is the first negative number.')
elif list1[2] < 0:
    print(list1[2], 'is the first negative number.')
elif list1[3] < 0:
    print(list1[3], 'is the first negative number.')
else:
    print('list1 has no negative numbers')