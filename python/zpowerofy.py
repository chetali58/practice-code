#code
def check(y,z):
    if(y!=1):
        while((z%y)==0):
            z=z/y;
    if(z==1):
        print('1')
    else:
        print('0')


     
    
x= int(input())
for i in range (0,x):
    inp= input()
    y= int(inp.split(' ')[0])
    z= int(inp.split(' ')[1])
    check(y,z)