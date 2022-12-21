# 4. Write a python program to add three numbers 25+’25’+25.0 and produce 
#    result 75 as string.

a = 25
b = '25'
c = 25.0

sum = str(a + int(b) + int(c))

print("sum is", sum)
print(type(sum))