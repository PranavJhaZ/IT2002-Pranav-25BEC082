# Part A - Q9: Tail recursion vs Iterative implementation


def sum_recursive_tail(lst, index=0, running_sum=0):
    if index >= len(lst):
        return running_sum
    return sum_recursive_tail(lst, index + 1, running_sum + lst[index])


def sum_iterative(lst):
    total = 0
    for item in lst:
        total += item
    return total


if __name__ == "__main__":
    nums = [3, 6, 9, 12, 15]
    print(f"List: {nums}")
    print("Recursive tail sum:", sum_recursive_tail(nums))
    print("Iterative sum:     ", sum_iterative(nums))
