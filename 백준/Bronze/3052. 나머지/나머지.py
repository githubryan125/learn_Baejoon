# 지얀스 a b 기 있을때 
# 나머지 
num=[0]*42
for i in range(10):
    n = int(input())
    num[n%42]=1
cnt=0
for k in num:
    if k != 0 :
        cnt+=1
print(cnt)