# n 명의 학생이 응시함
# 이들 중 상위 k 명은 상을 받는데 이때 커트라인

n,m=map(int,input().split())
score=list(map(int,input().split()))
score=sorted(score,reverse=True)

print(score[m-1])