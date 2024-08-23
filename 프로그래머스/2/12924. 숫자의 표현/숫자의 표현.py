def solution(n):
    answer = 0
    l = 1
    
    while l * (l - 1) // 2 < n:
        if (n - (l * (l - 1) // 2)) % l == 0:
            answer += 1
        l += 1
    
    return answer
