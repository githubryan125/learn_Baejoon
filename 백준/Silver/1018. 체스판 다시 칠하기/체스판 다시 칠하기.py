# 문제에서 2가지 방법 제시인데 나는 무조건 첫번째 문자를 기준으로만 생각했음
# 첫번째 문자가 잘못 입력 되었을 경우도 있는것을 간과함

N,M=map(int,input().split())
original=[]
count=[]

for _ in range(N):
    original.append(input())
for a in range(N-7):
    for b in range(M-7):
        index1=0
        index2=0
        
        for i in range(a,a+8):
            for j in range(b,b+8):
                if(i+j) %2==0:
                    if original[i][j] !="W":
                        index1+=1
                    if original[i][j] != "B":
                        index2 += 1
                else:
                    if original[i][j] !="B":
                        index1+=1
                    if original[i][j] != "W":
                        index2 += 1
        count.append(min(index1,index2))
print(min(count))