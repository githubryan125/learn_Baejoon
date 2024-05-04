# 온라인 저지에 가입한 사람의 나이와 이름이 순서대로 정렬한다
# 나이가 증가하는 수느올 나이가 같으면 먼저 가입한 사람이 먼저온다

#1. 나이를 기준으로 정렬
#2. 두번째 기준은 먼저 가입한 사람( 입력 순 )->< 인덱스

n=int(input())
custom=[]
for i in range(n):
    a,b=map(str,input().split())
    custom.append((a,b))
custom=sorted(custom, key=lambda x:(int(x[0]),x.index(x[1])))
for z,x in custom:
    print(z,x)