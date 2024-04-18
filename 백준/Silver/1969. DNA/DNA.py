# 각 위치에 들어갈 문자는 'A','G','T','C'로 총 4개이다.
# 이때는 각 문자의 위치마다 최대COUNT를 가지는 문자를 넣어주면 된다
# for 문을 돌면서 각 위치별 최빈 문자를 넣어주면 되고 이때 다른 문자를 가진
# 갯수의 합계를 구해주면 되는거 아닐까 ?
# 1969 번
n, m = map(int, input().split())

list = []
s = ''
dna = ['A', 'C', 'G', 'T']
hamming_distance = 0

for i in range(n):
    data = input()
    list.append(data)

for i in range(m):
    a_count, c_count, g_count, t_count = 0, 0, 0, 0
    for j in range(n):
        if list[j][i] == dna[0]:
            a_count += 1
        elif list[j][i] == dna[1]:
            c_count += 1
        elif list[j][i] == dna[2]:
            g_count += 1
        elif list[j][i] == dna[3]:
            t_count += 1
    count_list = [a_count, c_count, g_count, t_count]
    selected_dna = dna[count_list.index(max(count_list))]
    s += selected_dna
    for k in range(n):
        if list[k][i] != selected_dna:
            hamming_distance += 1

print(s)
print(hamming_distance)