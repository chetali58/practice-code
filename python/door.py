#code
import math
def door(y):
    return (math.floor(math.sqrt(y)) - math.ceil(math.sqrt(1)) + 1)
 

x= int(input())
for i in range (0,x):
    y= int(input())
    print(int(door(y)))