h, b, c, s = map(int, input().split())
hbcs = (h * b * c * s) / (8 * 1024 * 1024)
print(f"{hbcs:.1f} MB")