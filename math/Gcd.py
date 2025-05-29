# Greatest common factor of two numbers  

def gcd(a, b):
    while a !=  b:
        if a > b :
            a = a - b       
        else:
            b = b - a
    return a       

a = 4
b = 5
print(gcd(a, b))


# optimal way

def optimize(a, b):
    if b == 0 : 
        return a
    return  b * optimize(b,  a %b) 


optimize(a,b)
