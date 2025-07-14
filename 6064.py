a, b, c = map(int, input().split())
small = a if a < b and a < c else (b if b < c else c)
print(small)
