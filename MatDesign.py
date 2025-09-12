d,m=map(int,input().split())#m=dX3
if d%2==1:
    for i in range(1,d+1):
        if (d/2==(i-0.5)):
            print("WELCOME".center(m,'-'))
        elif (d/2>(i-0.5)):
            a=(2*i)-1    
            b=".|."*a
            print(b.center(m,'-'))
        else:
            b=".|."*a
            a-=2
            print(b.center(m,'-'))
