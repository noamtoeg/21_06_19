def pi_squared(rad):
    return rad**2*3.14

print(pi_squared(56))

def addition(x,y):
    return x+y


print(addition(4,6))

def myFactorial(x):
    factorial_list = list(range(x))
    fact = 1
    for n in factorial_list:
        n = n + 1
        fact = fact * n
    return fact

print(myFactorial(10))

def myCheckEven(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(myCheckEven(22))

def myAverage (l1):
    sum = 0
    count = 0
    for x in l1:
        sum = sum + x
        count = count + 1

    return sum/count

print(myAverage([2,8,10]))

def myConcat(s1,s2):
    return s1 + " " + s2

print(myConcat("hello","world"))
