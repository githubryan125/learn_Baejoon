def solution(s):
    answer = False
    if len(s) == 4 or len(s) ==6 :
        cnt=0
        for i in range(len(s)):
            if s[i] in ("0","1","2","3","4","5","6","7","8","9"):
                cnt+=1
                if cnt == len(s):
                    answer=True
    return answer