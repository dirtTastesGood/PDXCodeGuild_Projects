def fibonacci(iterations):
    fib = [1,1]
    for i in range(2, iterations):
        fib.append(fib[i-1] + fib[i-2])

    return fib

def main():
    iterations = 8
    print(f"The Fibonacci sequence to {iterations} places is: {fibonacci(iterations)}")

main()
