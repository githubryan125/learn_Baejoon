s=input()
char=[-1]*26

for i in range(len(s)):
    if char[ord(s[i])-ord('a')] ==-1:
        char[ord(s[i])-ord('a')]=i
print(*char)