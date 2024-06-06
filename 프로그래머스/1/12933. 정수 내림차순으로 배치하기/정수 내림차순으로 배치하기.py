def solution(n):
    answer = 0
    ans=sorted(str(n),reverse=True)
    k=""
    for i in ans:
        k+=i  
    answer=int(str(k))
    return answer