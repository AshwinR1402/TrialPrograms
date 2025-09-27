string=input()
k=int(input())
n=len(string) #k must be a factor of n
a=int(n/k) #int() is used bcoz on division we may get value with point i.e, for eg. 1.o
for i in range(1,a+1):
    b=string[(i-1)*k:i*k] #given str is seperated into n substr and each substr contains 'k' characters
    c=""
    for i in b:
        if c.count(i)==0: #each character of substr is appended to c after finding that there does wasn't the same character
            c+=i 
    print(c)
