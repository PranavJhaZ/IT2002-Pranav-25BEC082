# Part A - Q4: Recursive sorted order check


def check_sorted(elements, pos=0):
    if len(elements) <= 1 or pos >= len(elements) - 1:
        return True

    if elements[pos] > elements[pos + 1]:
        return False

    return check_sorted(elements, pos + 1)


if __name__ == "__main__":
    test1 = [1, 4, 9, 16, 25]
    test2 = [1, 9, 4, 16, 25]

    print(f"{test1} -> sorted:", check_sorted(test1))
    print(f"{test2} -> sorted:", check_sorted(test2))
