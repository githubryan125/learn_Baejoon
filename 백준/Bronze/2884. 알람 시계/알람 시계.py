# 45분 일찍 알람 설정하기
n,m = map(int,input().split())

if n==0 and m<45:
    n=23
    m+=60
if m < 45:
    n-=1
    m+=60
m=m-45
print(n,m,end=' ')