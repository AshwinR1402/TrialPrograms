n=int(input())
records=[]
for i in range(n):
    a=input()
    b=float(input())
    records.append(list((a,b)))   
c=[]
h=[]
for i in records:
    d=i[1]
    c.append(d)
e=min(c)
c=[x for x in c if x!=e] #Using remove() inside a loop may lead to skip some elements that is to be removed
f=min(c)
for i in records:
    if f in i:
        g=i.index(f)
        h.append(i[g-1])
        h.sort()
for i in h:
    print(i)
