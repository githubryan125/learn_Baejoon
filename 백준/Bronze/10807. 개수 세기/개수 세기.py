# n 개의 정수가 주어질때 정수 v 가 몇개인지 구해라
# n 주어지는 정수의 개수
# 정수가 공백으로 구분 
# 찾으려는 정수 v
n=int(input())
num=list(map(int,input().split()))
v=int(input())

cnt=0
for i in range(n):
    if num[i]==v:
        cnt+=1
print(cnt)