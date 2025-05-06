#method 1
def FibonacciRabbits(n, k):
    if n == 1 or n == 2:
        return 1
    prev_prev = 1
    prev = 1
    for month in range(3, n + 1):
        current = prev + k * prev_prev
        prev_prev = prev 
        prev = current
    return prev

N = 29
K = 5

#method 2
def fib(n, k):
    previous1, previous2 = 1, 1
    for i in range(2, n):
        current = previous1 + k * previous2
        previous2 = previous1
        previous1 = current
    return current

print(FibonacciRabbits(N, K))