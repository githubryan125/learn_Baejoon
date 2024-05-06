import sys
input=sys.stdin.readline

n,m=map(int,input().split())

book={}
for i in range(1,n+1):
    a = input().rstrip()
    book[i]=a
    book[a]=i
for j in range(m):
    b=input().rstrip()
    if b.isalpha():
        print(book[b])
    else:
        print(book[int(b)])