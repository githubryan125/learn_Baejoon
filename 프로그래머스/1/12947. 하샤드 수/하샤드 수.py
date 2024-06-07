def solution(x):
    answer = False
    hasa=0
    new_x=x
    while new_x >0:
        hasa+=new_x%10
        new_x//=10
    if x % hasa ==0:
        answer=True
    return answer