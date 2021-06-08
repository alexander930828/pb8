def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        else:
            i = i - 1

a = 60
b = 24

print(gcd(a, b))