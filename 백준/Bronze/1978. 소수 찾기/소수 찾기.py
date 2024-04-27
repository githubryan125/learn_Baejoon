# 주어진 수 n 개 중에서 소수가 몇개인가 ?
# 소수 : 나눠지는 수가 1과 자기 자신인 수

n = int(input())
number = list(map(int,input().split()))

for i in number:
    if i == 1:
        n=n-1
    else:
        for j in range(2,i):
            if i % j ==0:
                n=n-1
                break
print(n)