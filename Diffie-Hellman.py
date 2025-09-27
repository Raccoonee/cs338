
p = 103
g = 5

A=10
B=71


for a in range(1, 103):
    for b in range(1, 103):
        if ((g**b) % p) == A and ((g**a) % p) == B:
            print(f"a={a}, b={b}")
            print(f"Secret key: {(g**(a*b)) % p}")
            break