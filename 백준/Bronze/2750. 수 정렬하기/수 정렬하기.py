# 수 정렬하기
n = int(input())
num=[]
for i in range(n):
    num.append(int(input()))
num.sort()
for k in num:
    print(k,end="\n")