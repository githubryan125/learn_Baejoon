def solution(arr, divisor):
    answer = []
    cnt=0
    for i in arr:
        if i % divisor ==0:
            cnt+=1
            answer.append(i)
    answer.sort()
    if cnt==0:
        answer.append(-1)
    return answer