def solution(n, arr1, arr2):
    answer = []

    for i in range(n):

        bin_str = bin(arr1[i] | arr2[i])[2:] 
        bin_str = bin_str.zfill(n)
        decoded_row = bin_str.replace('1', '#').replace('0', ' ')

        answer.append(decoded_row)
    
    return answer