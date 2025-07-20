n = input().strip()
n_16 = int(n, 16)
for i in range(1, 16):
    print(f'{n}*{hex(i)[2:].upper()}={hex(n_16 * i)[2:].upper()}')