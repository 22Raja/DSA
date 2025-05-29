# Nive approach
def check_prime(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False       
    return True
get = int(input("Enter your number : "))
print(check_prime(get))

#O(n)
# Optimal approach

# 
def is_prime(n):
    if n == 1:
        return False
    i = 2 
    while(i * i <= n ):
        if (n % i == 0):
            return False
        i += 1
        
    else:
        return True


print("True")  if is_prime(get) else print("false")

# super efficient
def prime_is(n):
    if n == 1:
        return False
    if n  == 2 and n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5 
    while ( i *i <= n ):
        if n % i == 0 or n % ( i + 2 ) == 0:
            return False
        i += 6



prime_is()