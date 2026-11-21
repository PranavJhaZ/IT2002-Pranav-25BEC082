# Lab 2: Prefix Averages Comparison (Quadratic vs Linear)

import time
import math
import random


def prefix_avg_quadratic(values):
    count = len(values)
    averages = [0.0] * count
    for i in range(count):
        subtotal = 0.0
        for j in range(i + 1):
            subtotal += values[j]
        averages[i] = subtotal / (i + 1)
    return averages


def prefix_avg_linear(values):
    count = len(values)
    averages = [0.0] * count
    running_sum = 0.0
    for i in range(count):
        running_sum += values[i]
        averages[i] = running_sum / (i + 1)
    return averages


def compute_median_time(func, data, runs=5):
    timings = []
    for _ in range(runs):
        t_start = time.perf_counter()
        func(data)
        timings.append(time.perf_counter() - t_start)
    timings.sort()
    return timings[len(timings) // 2]


def run_tests():
    cases = [
        ("Empty input", []),
        ("Single value", [33.3]),
        ("Positive sequence", [3, 6, 9, 12, 15]),
        ("Negative sequence", [-1, -4, -7, -10]),
        ("Mixed sequence", [15, -5, 30, -10, 45]),
    ]
    print("Equivalence Tests:")
    for label, seq in cases:
        out_q = prefix_avg_quadratic(seq)
        out_l = prefix_avg_linear(seq)
        is_same = len(out_q) == len(out_l) and all(
            math.isclose(x, y, rel_tol=1e-9) for x, y in zip(out_q, out_l)
        )
        print(f"  {label:<18}: {'OK' if is_same else 'MISMATCH'} -> {[round(v, 2) for v in out_l]}")


def run_benchmarks():
    print("\nTiming Comparison:")
    sizes = [500, 1000, 2000, 4000, 8000]
    for n in sizes:
        test_arr = [random.uniform(1.0, 100.0) for _ in range(n)]
        t_quad = compute_median_time(prefix_avg_quadratic, test_arr)
        t_lin = compute_median_time(prefix_avg_linear, test_arr)
        speed = t_quad / t_lin if t_lin > 0 else 0
        print(f"  n = {n:<5} | Quadratic: {t_quad:.6f}s | Linear: {t_lin:.6f}s | Factor: {speed:.1f}x")


if __name__ == "__main__":
    run_tests()
    run_benchmarks()
