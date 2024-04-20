# 현재 시각
# 요리할때 필요한 시간

n,m = map(int,input().split())
time = int(input())

m=m+time
if m >= 60:
    n+=m//60
    m-=(m//60)*60
    if n >=24:
        n=n%24
print(n,m,end=' ')