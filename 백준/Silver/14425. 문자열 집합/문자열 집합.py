# 문자열 집합
# n 개의 문자열로 이뤄진 집합 S
# m 개의 문자열 중에서 집합 S
import sys
n,m = map(int,sys.stdin.readline().split())

s=dict()
cnt=0

for _ in range(n):
    word=sys.stdin.readline()
    s[word]=1
for _ in range(m):
    check=sys.stdin.readline()
    if check in s:
        cnt+=1
print(cnt)