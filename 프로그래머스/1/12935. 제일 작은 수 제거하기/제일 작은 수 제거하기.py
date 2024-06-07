def solution(arr):
    answer = []
    if len(arr)==1:
        answer.append(-1)
        return answer
    n = min(arr)
    arr.remove(n)
    return arr