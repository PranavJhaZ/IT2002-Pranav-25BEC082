# Part A - Q5: Naive recursive Fibonacci and recursion tree for n=5

calls = {}


def fibonacci(n):
    calls[n] = calls.get(n, 0) + 1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def show_tree():
    print("""
Recursion tree for fib(5):
                       fib(5)
                     /        \
              fib(4)            fib(3)
             /      \          /      \
        fib(3)      fib(2)    fib(2)  fib(1)
       /     \      /    \    /    \
    fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
    /    \
 fib(1) fib(0)
""")


if __name__ == "__main__":
    calls.clear()
    ans = fibonacci(5)
    print(f"fibonacci(5) = {ans}")
    show_tree()
    print("Subproblem invocation counts:")
    for k in sorted(calls.keys(), reverse=True):
        print(f"  fibonacci({k}): {calls[k]} calls")
