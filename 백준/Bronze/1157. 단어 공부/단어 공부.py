word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1: # 가장 많이 사용된 갯수가 같은 알파벳이 2개 이상
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])