# 과제 안내신분 ?
# 30명의 학생
# 28명만 과제 제출 이때 2명 안낸사람
num=[0]*31
num[0]=1
answer=[]
for i in range(28):
    n = int(input())
    num[n]=1
for j in range(1,31):
    if num[j]==0:
        answer.append(j)
print(answer[0])
print(answer[1])
