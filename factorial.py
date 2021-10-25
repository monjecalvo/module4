def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def factorial_rec(num):
    if num == 1:
        return 1
    return num*factorial_rec(num-1)

print(factorial(5))     
print(factorial_rec(5))