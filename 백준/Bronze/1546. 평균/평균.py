# 자기 점수중 최대 m 
# 모든 점 수를 점수/m* 100 으로 수정함 

n = int(input())
score=list(map(int,input().split()))

max_score=max(score)
for i in range(n):
    score[i]=(score[i]/max_score)*100
print(sum(score)/n)