# Lab 1: Algorithmic Growth Rates Benchmark

import time
import math
import random


def get_at_index(arr, i):
    return arr[i]


def binary_search(seq, key):
    start = 0
    end = len(seq) - 1
    while start <= end:
        middle = (start + end) // 2
        if seq[middle] == key:
            return middle
        elif seq[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
    return -1


def linear_search(seq, key):
    idx = 0
    for item in seq:
        if item == key:
            return idx
        idx += 1
    return -1


def mergesort(elements):
    if len(elements) <= 1:
        return elements
    mid = len(elements) // 2
    left = mergesort(elements[:mid])
    right = mergesort(elements[mid:])
    
    merged = []
    p1 = p2 = 0
    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]:
            merged.append(left[p1])
            p1 += 1
        else:
            merged.append(right[p2])
            p2 += 1
    if p1 < len(left):
        merged.extend(left[p1:])
    if p2 < len(right):
        merged.extend(right[p2:])
    return merged


def count_positive_pairs(arr):
    pairs = 0
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] + arr[j] > 0:
                pairs += 1
    return pairs


def generate_subsets(data):
    subsets = [[]]
    for element in data:
        subsets += [current + [element] for current in subsets]
    return subsets


def measure_runtime(func, *args, runs=5):
    durations = []
    for _ in range(runs):
        start = time.perf_counter()
        func(*args)
        durations.append(time.perf_counter() - start)
    durations.sort()
    return durations[len(durations) // 2]


def main():
    print("1. O(1) - List Index Lookup")
    for size in [10000, 50000, 100000, 250000, 500000]:
        data = list(range(size))
        elapsed = measure_runtime(get_at_index, data, size // 2)
        print(f"  size: {size:<8} | time: {elapsed:.8f}s")

    print("\n2. O(log n) - Binary Search")
    for size in [10000, 50000, 100000, 250000, 500000]:
        data = list(range(size))
        elapsed = measure_runtime(binary_search, data, -1)
        norm = elapsed / math.log2(size)
        print(f"  size: {size:<8} | time: {elapsed:.8f}s | T/log2(n): {norm:.2e}")

    print("\n3. O(n) - Linear Search")
    for size in [10000, 50000, 100000, 200000, 400000]:
        data = list(range(size))
        elapsed = measure_runtime(linear_search, data, -1)
        norm = elapsed / size
        print(f"  size: {size:<8} | time: {elapsed:.8f}s | T/n: {norm:.2e}")

    print("\n4. O(n log n) - Merge Sort")
    for size in [1000, 2000, 4000, 8000, 16000]:
        data = [random.randint(1, 100000) for _ in range(size)]
        elapsed = measure_runtime(mergesort, data)
        norm = elapsed / (size * math.log2(size))
        print(f"  size: {size:<8} | time: {elapsed:.8f}s | T/(n log n): {norm:.2e}")

    print("\n5. O(n^2) - Pair Counting")
    for size in [200, 400, 800, 1600, 3200]:
        data = [random.randint(-100, 100) for _ in range(size)]
        elapsed = measure_runtime(count_positive_pairs, data)
        norm = elapsed / (size ** 2)
        print(f"  size: {size:<8} | time: {elapsed:.8f}s | T/n^2: {norm:.2e}")

    print("\n6. O(2^n) - Subset Enumeration")
    for size in [10, 12, 14, 16, 18, 20]:
        data = list(range(size))
        elapsed = measure_runtime(generate_subsets, data, runs=3)
        norm = elapsed / (2 ** size)
        print(f"  size: {size:<8} | time: {elapsed:.8f}s | T/2^n: {norm:.2e}")

    print("\nSummary Table:")
    table = [
        ("List Index", "O(1)", "Constant access time"),
        ("Binary Search", "O(log n)", "Logarithmic efficiency"),
        ("Linear Search", "O(n)", "Linear scaling"),
        ("Merge Sort", "O(n log n)", "Divide-and-conquer linearithmic"),
        ("Pair Count", "O(n^2)", "Quadratic double-loop"),
        ("Subsets", "O(2^n)", "Exponential power set"),
    ]
    for algo, complexity, note in table:
        print(f"  {algo:<15} | {complexity:<10} | {note}")


if __name__ == "__main__":
    main()
