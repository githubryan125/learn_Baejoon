n,k=map(int,input().split())
arr=[i for i in range(1,n+1)]
answer=[]
cnt=0

for i in range(n):
    cnt += k-1
    if cnt >= len(arr):
        cnt =cnt%len(arr)
    answer.append(str(arr.pop(cnt)))
print("<",end="")
for i in answer:
    if answer[len(answer)-1]==i:
        print(i,end="")
        break
    print(i+",",end=" ")
print(">")