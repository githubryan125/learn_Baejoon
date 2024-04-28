# 네번째 점
dot = [list(map(int,input().split())) for _ in range(3)]
x=0
y=0
if dot[0][0]==dot[1][0]:
    x=dot[2][0]
elif dot[0][0]==dot[2][0]:
    x=dot[1][0]
elif dot[1][0]==dot[2][0]:
    x=dot[0][0]
if dot[0][1]==dot[1][1]:
    y=dot[2][1]
elif dot[0][1]==dot[2][1]:
    y=dot[1][1]
elif dot[1][1]==dot[2][1]:
    y=dot[0][1]
print(x,y,end=" ")