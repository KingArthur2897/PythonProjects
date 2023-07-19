from math import sqrt

def all_divisors(n):
    divisors = []
    for i in range(1, round(sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors
numbers = [23436, 190187200, 380457890232]
for i in range(len(numbers)):
    print(f"Divisors of {numbers[i]}:\n {all_divisors(numbers[i])}")
