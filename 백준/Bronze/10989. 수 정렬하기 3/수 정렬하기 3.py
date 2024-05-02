# n 개의 수가 주어질때 오름차순으로 정렬하는 프로그램
import sys
n=int(sys.stdin.readline())
num=[0]*10001
for i in range(n):
    num[int(sys.stdin.readline())]+=1

for j in range(1,10001):
    if num[j]!=0:
        for _ in range(num[j]):
            print(j)