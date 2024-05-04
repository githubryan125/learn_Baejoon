# 2 차원 평면 위에 점 n 개가 주어진다.
# 정렬은 x 좌표가 증가하는 순으로 정렬
# x 가 같으면 y가 증가하는 순으로 정렬

n=int(input())
a=[]
b=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append((x,y))
# 정렬
ans=sorted(a, key=lambda x: (x[0],x[1]))
for i in range(n):
    print(*ans[i])