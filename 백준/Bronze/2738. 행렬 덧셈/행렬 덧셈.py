# n  m 크기의 두 행렬이 있을때 두 행렬을 더해라
n,m=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
b=[list(map(int,input().split()))for _ in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j]=a[i][j]+b[i][j]
for k in range(n):
    print(*a[k])
    # print()