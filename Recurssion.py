#function for factorial 

# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))
 
 
#function for Fibonacci series/sequence
# f(0) = 0, f(1) = 1 , f(2) = f(1) + f(2) , f(n) = f(n-1)+f(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("enter number- "))
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")



