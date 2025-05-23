# What is Inheritance?

#To reuse code — don’t rewrite common features.

#To create a hierarchy of classes.

# To extend or customize the behavior of existing classes.





# Types of Inheritance

# Single Level Inheritance

# One child, One parent
class Animal:
    def speak(self):
        return "Animal Makes A sound"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


obj = Dog()
obj.speak()



# Multiple Inheritance

# One child, Multiple parents
class H: 
    def Think(self):
        return "I can Think"
class W:
    def Feel(self): 
        return "I can feel"
class C(H,W): 
    pass 


obj1 = C() 
print(obj1.Feel())


# Multilevel Inheritance

# Parent, Child, Grandchild

class A:
    def msg(self):
        return "A"

class B(A):
    pass

class C(B):
    pass

obj2 = C()
print(obj2.msg()) 


# Hierarchical Inheritance
# One parent, multiple children

class P: 
    def work(self):
        return "Working..." 
class Son(P):

    pass

class Daughter(P):
    pass  


obj3 = Daughter()
print(obj3.work()) 



# Hybrid Inheritance
#multiple + multilevel

class A:
    def work(self):
        return "Working from A"

class B(A):  # Multilevel starts here
    def manage(self):
        return "Managing from B"

class C(B):  # C extends the chain (A → B → C)
    def write(self):
        return "Writing from C"

class D(B):  # D is also a child of B (parallel to C)
    def read(self):
        return "Reading from D"

class E(C, D):  # Multiple inheritance from both C and D
    def play(self):
        return "Playing from E"

# Create object
obj = E()
print(obj.work())   # From A
print(obj.manage()) # From B
print(obj.write())  # From C
print(obj.read())   # From D
print(obj.play())   # From E







