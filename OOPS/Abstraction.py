from abc import ABC , abstractmethod


class Car(ABC): 
    @abstractmethod
    def Drive(self): 
        pass 
    
    def Color(self): 
        return "The Color is RED"


# Concrete subclass
class Bmw(Car):
    def Drive(self):
        return "Raja Have Benz"

# Concrete subclass
class Audi(Car):
    def Drive(self):
        return "Raja Have Audi"



def cars(obj):
    for i in obj: 
        print(i.Drive())  

collection = [Bmw() , Audi()] 
cars(collection) 


#we are Hiding Implementation of the complex code , so it’s simple to use by calling the interface 
#Well structured , Follow Rules So we avoid error in implementing the methods 
      
# Eg - Car we see break, gear but the implementation for each Brands. Its different Abstract class helps us to Hide each brand Implementation by providing an Interface . 

