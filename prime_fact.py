def prime_factors(n):
    factors = {}
    d = 2

    while n > 1:
        if n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n = n // d
        else:
            d += 1

    return factors


def main():
    num=int(input("Enter the number: "))
    d1=prime_factors(num)
    print(d1)

main()