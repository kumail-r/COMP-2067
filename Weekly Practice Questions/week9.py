list1 =[2, 4, 6, 3]
w = 1
x = 4
y = 2
z = 5

for item in list1:
  w = w + 2*item
  if w > 10:
    break
print(w)

val = 0
for num in list1:
    if num > 5:
        continue
    else:
        val += num
print(val) 

for i in range(3, 30, 2):
  z = z + i
  x = x + 1
  y = x + z
print(x,y,z)