n = int(input())
k = int(input())

k1 = k%10
k2 = (k//10)%10
k3 = k//100
print(k1*n)
print(k2*n)
print(k3*n)
print(k*n)