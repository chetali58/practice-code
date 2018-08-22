#code
def gcd(y,z):
    if(y==z):
        return y
    if(y>z):
        return gcd(y-z,z)
    return gcd(y,z-y)
    
def lcm(y,z):
    return int(y*z/gcd(y,z))
    
    
x= int(input())

for i in range (0,x):
    inp= input()
    y= int(inp.split(' ')[0])
    z= int(inp.split(' ')[1])
    print (str(lcm(y,z)) +' '+ str(gcd(y,z)))
     
