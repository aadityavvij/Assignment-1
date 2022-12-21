# 3. Write a program that asks the user for a number of seconds and prints out 
#    how many minutes and seconds that is. For instance, 200 seconds is 3 
#    minutes and 20 seconds.

a = int(input("Enter the time in seconds\n"))

min = a//60
sec = a%60

print(f"{a} seconds corresponds to {min} minutes and {sec} seconds")