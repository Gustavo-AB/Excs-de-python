def fatorial(num):
    fat = 1
    for c in range(num, 0, -1):
        print(f'{c} x', end=" ")
        fat *= c

    return fat

