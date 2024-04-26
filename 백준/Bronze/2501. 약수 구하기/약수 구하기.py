# n 의 약수중 k 번째로 작은 수를 출력한다.

n,m=map(int,input().split())

num=[]

for i in range(1,n+1):
    if n%i==0:
        num.append(i)
if len(num) < m:
    print(0)
else: print(num[m-1])


