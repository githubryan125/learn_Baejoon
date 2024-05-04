# 알파벳 소문자로 이뤄진 n 개의 단어
# 1. 길이가 짧은거 부터
# 2. 길이가 같으면 사전순으로 (ascil 코드순)
n=int(input())
ans=[]
for i in range(n):
    ans.append(input())
ans=list(set(ans))
answer=sorted(ans, key=lambda x:(len(x),x))

for k in answer:
   print(k)