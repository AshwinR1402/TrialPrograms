n=int(input())
if n%2==1:
    for i in range(1,2*n,2):
        a="H"
        b=a*i
        print(b.center((2*n)-1," ")) 
    for i in range(1,n+2):
        a="H"*n
        print(a.rjust(int(((3*n)-1)/2)," "),a.rjust((4*n)-1," "))      
    for i in range(1,int((n+3)/2)): 
        a="H"*n*5
        print(a.rjust(int((5*n)+(n-1)/2))," ")     
    for i in range(1,n+2):
        a="H"*n
        print(a.rjust(int(((3*n)-1)/2)," "),a.rjust((4*n)-1," "))
    for i in range((2*n)-1,0,-2):
        a="H"
        b=a*i    
        print(b.center((10*n)-1," "))
