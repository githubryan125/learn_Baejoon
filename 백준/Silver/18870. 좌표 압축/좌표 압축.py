# 좌표 압축

# 수직선 위에 n 개의 좌표가 있다
# Xi를 압축한 Xi' 는 Xi>Xj를 만족하는 서로 다른 좌표  Xj의 개수와 같아야 한다.
# 좌표압축을 사용한 결과를 출력력

# 제일 작은 수 0
# 그 다음으로 작은 수 1
# 결국 수 끼리 순서를 정해주는 ?
# 처음에 중복제거해서 정렬해줘 그다음에 순서를 대입시켜 그냥
import sys

n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))

number=sorted(set(num))

answer={cord: index for index, cord in enumerate(number)}

for cord in num:
    print(answer[cord], end=" ")