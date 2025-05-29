def divisor(get):
    number = []
    for i in range(1 , get+1):
        if get % i == 0:
            number.append(i)
    else:
        return number
# o(n)
# o(1)
def divisor_get(get):
    i = 1
    while (i * i < get ):
        if (get % i == 0):
            print(i) 
        i += 1
    while (i >= 1 ):
        if ( get %i == 0  ):
            print(get//i)
        i -=1  
    


get = int(input("Enter your number"))
print(divisor(get))