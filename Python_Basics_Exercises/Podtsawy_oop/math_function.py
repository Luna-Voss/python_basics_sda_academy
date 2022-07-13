

def into_fraction(x):
    l = x
    m = 1
    while not l.is_integer():
        l = l*10
        m = m*10

    return print(f"{int(l)}/{m}")

into_fraction(0.6756)

def nwd_i(a, b):
    while b:
        temp = a
        a = b
        b = temp%b
    return a

nwd_i(6, 9)

