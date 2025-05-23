class Bank: 
    # Constructor    
    def __init__(self,owner, balance):
        self.owner = owner         #Public Attribute   
        self.__balance = balance   #Private Attribute 
    
    #Getter Method to Access Private data
    def get_balance(self):
        return self.__balance

    #Setter Method with Validation
    def deposite(self , amount):
        if amount > 0 : 
            self.__balance += amount 
            return f"Deposited: {amount}"
        else: 
            return "Deposit Amount Must be Positive! " 
    
    #Setter Method with Validation
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount   
            return f"Withdrew: ${amount}"
        else:
            return "Insufficient balance or invalid amount." 

# --- Test the class ---


account = Bank("Raja", 1000)

print(f"Owner: {account.owner}")
print(f"Balance: {account.get_balance()}")  # Safe access

print(account.deposite(1000) ) 

print(f"Balance: {account.withdraw(25)}")  # Safe access

 
     
#What is Encapsulation ?  
#Code is Reusable   
#Safe and structured code 
#Protecting variables and structuring code safely.

# Class is a Plan
# Object is a Product 