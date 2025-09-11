x=int(input())
y=int(input())
z=int(input())
n=int(input())
d=[]
d1=[[x1,y1,z1] for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1)]
for a in d1:
    i=0
    for b in a:
        i+=b
    if i!=n:
        d.append(a)      
print(d)
