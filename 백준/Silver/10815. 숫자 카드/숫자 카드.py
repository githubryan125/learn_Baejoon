# 숫자 카드는 하나가 적혀있음
# 상근이는 숫자 n 개
# 정수 m 개가 주어질때
# 이후 정수 m 개가 주어질때 이 수가 적혀 있는 숫자 카드를 상근이가 갖고있나?
import sys

n=int(sys.stdin.readline())
num1=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
num2=list(map(int,sys.stdin.readline().split()))

_dict={}
for i in range(n):
    _dict[num1[i]]=0

for j in range(m):
    if num2[j] in _dict:
        print(1,end=" ")
    else:
        print(0,end=" ")