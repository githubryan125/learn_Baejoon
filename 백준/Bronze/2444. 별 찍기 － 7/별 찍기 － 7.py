n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),"*"*i,"*"*(i-1),sep='')
for j in range(n-1,0,-1):
    print(" " * (n - j), "*" * j, "*" * (j - 1), sep='')