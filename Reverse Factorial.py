from math import factorial as f

inputnum = int(input("Input number to perform inverse factorial with\n"))
def factorial_cap(num):
    n, i=1, 1
    while n <= num: i += 1; n *= i
    return i
print(factorial_cap(inputnum)-1)
print(f(factorial_cap(inputnum)-1))