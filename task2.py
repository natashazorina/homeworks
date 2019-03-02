N = int(input())
m = N // 1000
k = N % 10
l = N // 100 - m * 10
h = (N % 100 - k) // 10
G = m * 10 + l
F = k * 10 + h
print(int(G == F))
