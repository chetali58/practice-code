#code
def power(y):
    if((y>0) and (y&(y-1)==0)):
        print('YES')
    else:
        print('NO')


x= int(input())
for i in range (0,x):
    power(int(input()))

    