def func(number):
    get = 1
    if number  == 0:
        return 1 
    for i in range(number ,  1  , -1):
        print(i) 
        get *= i
    
    return get 
n = int(input('Enter your number :'))

print(f"Factorial of  {n} is :  {func(n)}")

# Recursion factorial 

def rec_fact(number):
    if number  == 0:
        return 1 

    return number * rec_fact(number - 1)


print(rec_fact(5))


# 5  * (5- 1)
# 4  * (4 - 1)
# 3  * (3 - 1)
# 2  * (2- 1)
# 1  * (1 - 1)



