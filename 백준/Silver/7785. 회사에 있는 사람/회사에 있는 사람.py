# 문자열 집합
# n 개의 문자열로 이뤄진 집합 S
# m 개의 문자열 중에서 집합 S
import sys
n = int(sys.stdin.readline())

s=dict()
cnt=0
ans={}
for i in range(n):
    word,work=map(str,sys.stdin.readline().split())
    if work == "enter":
        ans[word]=1
    if work == "leave":
        ans.pop(word)
ans=sorted(ans,key=lambda x:x,reverse=True)
for a in ans:
    print(a)

#  시간초과시 딕셔너리 사용