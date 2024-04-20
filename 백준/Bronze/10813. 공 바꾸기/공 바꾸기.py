# 바구니 n 개
# 각 바구니 에는 1~n 번까지 번호가 있다

n, m =map(int,input().split())
num=[0]*(n+1)
for i in range(1,n+1):
    num[i]=i

tmp=0
for j in range(m):
    a,b=map(int,input().split())
    tmp=num[a]
    num[a]=num[b]
    num[b]=tmp
num.pop(0)
print(*num)