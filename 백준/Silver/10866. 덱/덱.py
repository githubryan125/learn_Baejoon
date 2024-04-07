from collections import deque
# import sys
# input=sys.stdin.readline()

d =deque()
n = int(input())
command = [list(input().split()) for _ in range(n)]


for i in range(n):
    if command[i][0] == "push_front":
        d.appendleft(command[i][1])
    elif command[i][0] == "push_back":
        d.append(command[i][1])
    elif command[i][0] == "pop_front":
        if len(d)==0:
            print(-1)
            continue
        print(d.popleft())
    elif command[i][0] == "pop_back":
        if len(d) == 0:
            print(-1)
            continue
        print(d.pop())
    elif command[i][0] == "size":
        print(len(d))
    elif command[i][0] == "empty":
        if len(d) == 0:
            print(1)
        else: print(0)
    elif command[i][0] == "front":
        if len(d)==0:
            print(-1)
            continue
        print(d[0])
    elif command[i][0] == "back":
        if len(d) == 0:
            print(-1)
            continue
        print(d[len(d)-1])