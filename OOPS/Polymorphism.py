# Why use Polymorphism?
 
# Polymorphism means “many forms”
# In OOP, it allows the same method name to behave differently based on the object calling it called 
# Makes code Flexible 
# It Follows the Open/Closed Principle 


# Method Overriding 
# Duck Typing
# Operator OverLoading 


# Method Overriding 

class person1: 
    def write(self): 
        return " I can write English "


class person2(person1): 
    def write(self): 
        return " I can write Tamil "


obj = person2()
print(obj.write()) 



# Duck Typing 
class Dog: 
    def Speak(self):
        return "Dog bark" 

class People: 
    def Speak(self):
        return "People Talk"



def taking(obj):
    return obj.Speak() 
 
print(taking(Dog()))      
print(taking(People()))    


# Operator OverLoading 

class Book: 
    def __init__(self , pages):
        self.pages = pages 
    def __add__(self , other):
        return Book(self.pages + other.pages )
    def __str__(self):
        return f"The Book Total pages :- {self.pages} "
    


A = Book(50)

B = Book(40) 

print(A+B)


# Method Over Loading 