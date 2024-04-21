# 숫자 하나 누르고 금속핀 있는데 까지 시계방향으로 돌려야한다.
# 숫자 하나 누르면 다이얼 초기화
# 숫자 1은 2초 이후 숫자는 +1 추가
#  2 3 4 5 6 7 8 9 10 11 초
#  1 2 3 4 5 6 7 8 9  0

s = input()
call=0
for i in range(len(s)):
    if s[i]=='A' or s[i]=='B' or s[i]=='C':
        call+=3
    elif s[i]=='D' or s[i]=='E' or s[i]=='F':
        call+=4
    elif s[i]=='G' or s[i]=='H' or s[i]=='I':
        call+=5
    elif s[i]=='J' or s[i]=='K' or s[i]=='L':
        call+=6
    elif s[i]=='M' or s[i]=='N' or s[i]=='O':
        call+=7
    elif s[i]=='Q' or s[i]=='R' or s[i]=='S' or s[i]=='P':
        call+=8
    elif s[i]=='T' or s[i]=='U' or s[i]=='V':
        call+=9
    elif s[i]=='W' or s[i]=='X' or s[i]=='Y' or s[i]=='Z':
        call+=10
print(call)