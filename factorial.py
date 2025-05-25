def factorial():
    n = int(input("Enter a number: "))
    res = 1
    for i in range(1, n + 1):
        res *= i
    print("Factorial of", n, "is:", res)
factorial()