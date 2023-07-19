from decimal import Decimal

num = Decimal(input("Input number:\n"))

digits = num.as_tuple().digits

print(sum(digits))