# 너의 평점은
# 전공 평점 전공 ㅘ목 학점 x 과목평점 의 합을 학점의 총합으로 나눈다.

grade = [list(input().split()) for _ in range(20)]
sum=0
classes=0
for i in range(len(grade)):
    if grade[i][2]=="A+":
        grade[i][2]=4.5
    elif grade[i][2]=="A0":
        grade[i][2]=4.0
    elif grade[i][2]=="B+":
        grade[i][2]=3.5
    elif grade[i][2]=="B0":
        grade[i][2]=3.0
    elif grade[i][2]=="C+":
        grade[i][2]=2.5
    elif grade[i][2]=="C0":
        grade[i][2]=2.0
    elif grade[i][2]=="D+":
        grade[i][2]=1.5
    elif grade[i][2]=="D0":
        grade[i][2]=1.0
    else:
        if grade[i][2]=="P":
            grade[i][1]=0.0
        grade[i][2]=0.0
    sum+=float(grade[i][1])*float(grade[i][2])
    classes+=float(grade[i][1])

print(sum/classes)
