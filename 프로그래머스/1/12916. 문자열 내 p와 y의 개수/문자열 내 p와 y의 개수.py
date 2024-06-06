def solution(s):
    cnt_p,cnt_y=s.count('p')+s.count('P'),s.count('Y')+s.count('y')    
    if cnt_p == cnt_y:
        return True
    else: return False