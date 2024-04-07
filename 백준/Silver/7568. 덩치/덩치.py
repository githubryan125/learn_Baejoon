n= int(input())
heavy=[list(map(int,input().split())) for _ in range(n)]

rank=0
for i in range(n):
    rank=1
    for j in range(n):
        if heavy[i][0] < heavy[j][0] and heavy[i][1] < heavy[j][1]:
            rank+=1
    print(rank,end=" ")