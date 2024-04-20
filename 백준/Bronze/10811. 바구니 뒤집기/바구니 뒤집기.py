# 바구니 n 개 1 ~ n 왼쪼부터 1
# 도현이는 앞으로 m번 바구니의 순서를 역순으로 만들거다
#
n,m=map(int,input().split())
num=[0]*(n+1)

for e in range(1,n+1):
    num[e]=e
tmp=0
for i in range(m):
    a,b=map(int,input().split())
    for j in range((b-a+1)//2):
        tmp=num[a+j]
        num[a + j]=num[b-j]
        num[b - j]=tmp
    
num.pop(0)
print(*num)

# 1 2 3 4 5
# 1 2 3 4 5
# 2 1 3 4 5
# 2 1 4 3 5
# 3 4 1 2 5
