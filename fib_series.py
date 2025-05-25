def fib():
    n=int(input("enter the no. of terms required in Fibonacci Series:"))
    a=0
    b=1
    for i in range(n):
        print(a)
        res=a+b        
        a=b
        b=res
        
fib()

