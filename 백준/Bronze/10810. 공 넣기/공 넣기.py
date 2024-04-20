# 바구니 n 개
# 각 바구니 에는 1~n 번까지 번호가 있다
# 또 1~n 까지 번호가 있는 공을 많이 갖고 있다
# 가장 처음 바구니에는 공이 없으며 바구니에는 공을 1개만 넣을수 있다.
# 도현이는 앞으로 m번 공을 넣을라고 한다.

#1 2 3 4 5
#1 2 1 1 0

n , m =map(int,input().split())
num=[0]*n
for i in range(m):
    ball=list(map(int,input().split()))
    for j in range(ball[0]-1,ball[1]):
        num[j]=ball[2]
print(*num)