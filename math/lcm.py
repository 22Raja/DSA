# least common factor


def least(a, b):
    res = max(a,b)

    while True:
        if  res % a == 0   and res % b == 0 :
            return res
        res += 1
    return res

a, b = 4 ,6
least(a , b) 


def lcm(a , b):

    def gcf(a, b):
        if b == 0 :
             return a

        return gcf( b ,  a % b)
    
    return a//b  * gcf(a , b)

print(lcm(a, b))