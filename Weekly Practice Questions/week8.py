list1 =[7, 0, -1, 2]
w = 0
x = 4
y = 15
z = -2
while y > z:
    z = z + x
    y -=1
    x += 1
print(x,y,z)

list1 =[7, 0, -1, 2]
w = 0
x = 4
y = 15
z = -2
while y > list1[2]:
    y -=2
    w = w+1
print(w,y,z)

list1 =[7, 0, -1, 2]
w = 0
x = 4
y = 15
z = -2
while True:
  if w >= len(list1):
    break
  if list1[w] < 0:
    w += 1
    continue
  else:
    z = z + list1[w]
    y += 1
    w += 2
print(w,x,y,z)