# AC
# R 뒤집기 D 버리기  배열의 수 순서 뒤집기, 배열의 첫번째 수 버리기
# 단 배열이 비어있을때 D 쓰면 에러남 -> 실제로 버리지 않고 "error 출력"
# 함수는 조합가능하다
from collections import deque
t = int(input())
for i in range(t):
    # 수행할 함수
    p=input()
    # 배열에 있는 원소의 수
    n=int(input())
    arr=input()[1:-1].split(',')
    queue = deque(arr)
    flag=0
    if n ==0 :
        queue=[]
    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(queue) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")

