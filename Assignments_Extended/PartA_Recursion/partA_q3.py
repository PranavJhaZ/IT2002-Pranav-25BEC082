# Part A - Q3: In-place sequence reversal with trace


def reverse_range(data, left, right):
    if left >= right:
        return

    print(f"Swapping indices {left} and {right}: {data[left]} <-> {data[right]}")
    data[left], data[right] = data[right], data[left]

    reverse_range(data, left + 1, right - 1)


if __name__ == "__main__":
    sequence = [11, 22, 33, 44, 55, 66]
    print(f"Initial sequence: {sequence}\n")
    reverse_range(sequence, 0, len(sequence) - 1)
    print(f"\nReversed sequence: {sequence}")
