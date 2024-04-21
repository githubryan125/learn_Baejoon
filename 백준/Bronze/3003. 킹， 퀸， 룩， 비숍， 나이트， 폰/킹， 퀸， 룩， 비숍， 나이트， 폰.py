# 16 개의 파츠 킹 1 퀸 1 룩 2 비숍 2 나이트 2 폰 8
# 검정은 모두 있지만 흰색은 몇개 없음 
# 동혁이가 발견한 흰색 피스가 주어질때 몇개를 더 하거나 빼야 올바른 세트가 되는가?

n=list(map(int,input().split()))
ans=[1,1,2,2,2,8]

for i in range(6):
    ans[i]-=n[i]
print(*ans)