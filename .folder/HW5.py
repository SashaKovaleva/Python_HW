def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return 1 + sum(a-1, b-1)

a = 2
b = 2
print(sum(a, b))