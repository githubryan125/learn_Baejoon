# n 개의 수가 주어질때 오름차순으로 정렬하는 프로그램
import sys
n=int(input())
num=[]
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

for j in num:
    print(j)