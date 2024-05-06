import sys
input=sys.stdin.readline

n=int(input())
card=list(map(int,input().split()))
m=int(input())
mine=list(map(int,input().split()))

dit={}
for i in card:
    if i in dit:
        dit[i]+=1
    else:
        dit[i]=1
for i in mine:
    if i in dit:
        print(dit[i],end=" ")
    else:
        print(0,end=" ")