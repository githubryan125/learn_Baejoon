t = int(input())
for _ in range(t):
    answer=''
    a,b=map(str,input().split())
    for i in range(len(b)):
        answer+=b[i]*int(a)
    print(answer)