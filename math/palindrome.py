#  Check palindrome

def ispal(number):

    temp = number 
    reverse = 0 

    while number > 0:
        reverse = reverse * 10 
        reverse += number % 10       
        number = number //10    

    if  temp == reverse: 
        return True 
    else: 
        return False 



if __name__ == "__main__":
    number = 5355
    print(ispal(number))
