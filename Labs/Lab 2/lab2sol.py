# Written by Kumail Raza (105225432) on 2/4/2022

x = 3 # declare x
print('x = ' + str(x)) # print value of x
x = float(x) # convert x to float
print('After converting to float: x = ' + str(x)) # print updated value of x

y = -9.677 # declare y
print('y = ' + str(y)) # print value of y

z = pow(y,x) # declare z as being y^x
print('The value of y**x is: z = ' + str(z)) # print value of z

z = round(z,3) # round z to 3 decimals
print('The value of z rounded to 3 decimal places = ' + str(z)) # print updated value of z

print('The absolute value of z is: ' + str(abs(z))) # print absolute value of z

result = (x*y+7)/(x+y) # calculate and store (x*y+7)/(x+y) into result
print('The result rounded to the nearest integer is: ' + str(int(result))) # print value of result rounded to the nearest integer
