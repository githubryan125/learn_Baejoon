n = int(input())
if n==1:
    exit()
for i in range(2,n+1):
    if n==0:
        break
    if n % i ==0:
        while n % i ==0:
            n=n//i
            print(i)
