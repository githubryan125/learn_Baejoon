# 수행 횟수
n=int(input())
cnt=0
for i in range(1,n):
    cnt+=i
print(cnt)
print(2)


# 1 2 3 4 5 6   6
# 2 3 4 5 6     5
# 3 4 5 6       4 
# 4 5 6         3
# 5 6           2
# 6             1