# list로 받아
# 마지막 줄은 0 0 0
while True:
    try:
        tri=list(map(int, input().split()))
        if tri.count(0)==3:
            exit()
        if max(tri) >= tri[0]+tri[1]+tri[2]-max(tri):
            print("Invalid")
            continue
        if tri[0]==tri[1]==tri[2]:
            print("Equilateral")
        elif tri[0]==tri[1] or tri[1]==tri[2] or tri[0]==tri[2]:
            print("Isosceles")
        elif tri[0]!=tri[1] and tri[1]!=tri[2] and tri[0]!=tri[2]:
            print("Scalene")
    except:
        exit()
