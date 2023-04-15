def fatorial(n, show=False):
    f = 1
    for c in range(1, n + 1):
        f *= c
        if show:
            if c < n:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return f


print(fatorial(4, show=True))

