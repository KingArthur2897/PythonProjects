from math import sqrt

def calc(sum, mul):
    d = sum * sum + 4 * mul
    if d > 0:
        sq = sqrt(d)/2
        p = sum/2
        x1 = p - sq
        x2 = p + sq
        return [x1,x2]

S = int(input("Input sum:\n"))
P = -int(input("Input mul:\n"))
print(calc(S,P))