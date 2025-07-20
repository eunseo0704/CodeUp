n = int(input())
s = 0 
c = 1
while True:
    s += c
    if s >= n:
        break
    c += 1
print(s)