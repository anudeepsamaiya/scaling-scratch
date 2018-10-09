import sys

# 3
# 1 2 3
# 1 3 2
# 2 1 3
num = int(input().strip())
for a0 in range(num):
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]
    if (-(z-y)) == (z-x):
        print('Mouse C')
    elif z-y < z-x:
        print('Cat B')
    else:
        print('Cat A')
