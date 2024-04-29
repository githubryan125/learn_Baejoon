# # 수행 횟수
n=int(input())
cnt=0
for i in range(1,n-1):
    cnt+=i*(n-1-i)
print(cnt)
print(3)   # for문 3개임

# i = 1 ~ n-2
# j = i+1 ~ n-1
# k = j+1 ~ n

# i 가 1 2 3 4 5
#      2 3 4 5
#      34567  5 4 3 2 1  4 3 2 1
#print(5+4*2+3*3+2*4+1*5)