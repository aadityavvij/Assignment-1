# 5. Write a program that prints out the sine and cosine of the angles ranging 
#    from 0 to 345◦ in 15◦ increments. Each result should be rounded to 4 
#    decimal places.

import math

d = 0

while(d<=345):
    r = math.radians(d)  #converting degrees to radians
    sine = round(math.sin(r), 4)  #finding sine and rounding off
    cosine = round(math.cos(r), 4)  #finding cosine and rounding off
    print(f"{d} --- {sine}  {cosine}")  #printing in desired format
    d = d + 15