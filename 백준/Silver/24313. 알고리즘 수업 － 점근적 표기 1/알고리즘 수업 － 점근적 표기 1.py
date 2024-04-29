# 점근적 표기
# f(n)= a1*n + a0
a1,a0 =map(int,input().split())
g1=int(input())
c=int(input())

if (a1*c+a0) <= g1*c and a1<=g1:
    print(1)
else: print(0)

