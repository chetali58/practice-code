#code
import math
def ang(h,m):
    if(h==12):
        h=0
    if(m==60):
        m=0
    ha= 0.5*(h*60 + m)
    ma= m*6
    a= abs(ha-ma)
    ap= min(a,360-a)
    af= math.floor(ap)
    return af
    
    
x= int(input())
for i in range (0,x):
    inp= input()
    h= int(inp.split(' ')[0])
    m= float(inp.split(' ')[1])
    print(ang(h,m))
    
