for i in range(1,int(input())):
    print(i*((10**i)//9))
"""How? Let us break it into three segment for each iteration.
10**i gives the value of   10 to the power i (ie.10^i) .At i=1(10^i gives value 10)
(10**i)//9 gives the remainder 1,11,111..... until N=10 
i*((10**i)//9) gives i*1,i*11,i*111,....."""
