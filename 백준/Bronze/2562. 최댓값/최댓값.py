# 9개의 서로 다른 자연수 중 최대값을 찾고 그 최대값이 몇번째 수인가?
num=[]
for i in range(9):
    num.append(int(input()))
print(max(num))
print(num.index(max(num))+1)