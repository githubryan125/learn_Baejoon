def solution(num):
    answer = -1
    if num == 0 or num ==1:
        return 0
        
    for i in range(499):
        if num % 2==0:
            num//=2
            if num == 1:
                answer=i+1
                break
        else:
            num*=3
            num+=1
            if num == 1:
                answer=i+1
                break
    return answer