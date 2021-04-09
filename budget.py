class Budget:
    def __init__(self, name, bal): 
        self.__name = name
        self.__balance = bal
    def deposit(self, amount,):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= int(amount)
        else:
            print('Error: Insufficient funds') 
    def transfer(self, amount, name):
        if self.__balance != 0:
            self.withdraw(amount)
            name.deposit(amount) 
        else:
            print('Error: Insufficient funds')                  
    def getbalance(self):
        return self.__balance 
               
