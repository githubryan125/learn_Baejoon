number=[list(map(int,input().split()))for _ in range(9)]

max_cnt=0
a,b=0,0
for i in range(9):
    for j in range(9):
        if max_cnt <= number[i][j]:
            max_cnt=number[i][j]
            a,b=i+1,j+1
print(max_cnt)
print(a, b)