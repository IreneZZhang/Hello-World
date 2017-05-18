def fibonacci(n):
     """gives the nth fibonacci number"""
     if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

