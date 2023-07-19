n = int(input("Input limit of powers of two\n"))

def powers(limit):
    t = 2
    while t <= limit:
        print(t)
        t*=2

powers(n)
