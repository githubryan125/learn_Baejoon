# 도화지 100 100
# 색종이 10 10 이때 색종이가 붙은 면적을 구하라라
# 관건은 겹치는 부분을 어떻게 생각할 것인가?
n = int(input())
white = [[0]*100 for _ in range(100)]
cnt=0

for i in range(n):
    a,b=map(int,input().split())
    for j in range(10):
        for h in range(10):
            if white[a+j][b+h]==1:
                cnt+=1
            elif white[a+j][b+h]==0:
                white[a+j][b+h]=1

print((100*n)-cnt)
