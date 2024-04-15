# 잘못된 수를 부르면 0을 말해서 가장 최근에 쓴수를 지운다.
n=int(input())
num=[]
for i in range(n):
    a=int(input())
    if a==0:
        num.pop()
    else:
        num.append(a)
print(sum(num))