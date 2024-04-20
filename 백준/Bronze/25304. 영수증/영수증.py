# 물건의 가격이 수상하다
# 영수증의 총 금액 x
# 물건의 종류의 수  n
#  물건의 가격 a 와 개수 b 가 나옴

x= int(input())
n = int(input())
product=[list(map(int,input().split()))for _ in range(n)]
x_all=0
for j in range(n):
    x_all+=product[j][0]*product[j][1]
if x == x_all:
    print("Yes")
else: print("No")