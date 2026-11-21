# Part A - Q2: Recursive Factorial, Sum of Natural Numbers, and Power


def factorial(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def natural_sum(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        return 0
    return n + natural_sum(n - 1)


def power(base, exp):
    if exp < 0:
        raise ValueError("Exponent must be non-negative")
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Sum of first 10 numbers:", natural_sum(10))
    print("2 to the power 8:", power(2, 8))
