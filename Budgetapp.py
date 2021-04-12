# Okolie Martin 
# Budget app 


#This is the class budget
class Budget:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

# This is the function that enables deposting funds
    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Your current balance in {self.name} budget is {self.balance} naira"

#This function enables withdrawal if funds
    def withdrawal(self, withdrawalAmount):
        if self.balance < withdrawalAmount:
            print(f"There is not enough money in{self.name} budget for this transaction" )
        else:
            self.balance = self.balance - withdrawalAmount
            return f"You have succesfully withdrawn funds from {self.name} budget and your current balance is {self.balance} naira"

# This function enables display of current balance
    def moneyAvailable(self):
        return f"Your current available balance in {self.name} budget is {self.balance} naira"

        
# This function enables trandfer of funds between the budget categories
    def transfer (self, sendingAmount, sendTo):

        if self.balance < sendingAmount:
            print(f"There is not enough funds in {self.name} for this transaction")

        else:
            self.balance = self.balance - sendingAmount
            sendTo.balance = sendTo.balance + sendingAmount

            feedback = f"You have succesfully transfered funds to {sendTo.name} budget and your current balance is {sendTo.balance} naira"
            return feedback




# These instantiate the budget categories
feedingBudget = Budget("food" , 5000)
clothingBudget = Budget("clothes", 3000) 
entertainment = Budget("entertainment", 4000)


# Please comment out the code below to see how everything works 
#  print (feedingBudget.deposit(550))
#  print (feedingBudget.withdrawal(500))
#  print (clothingBudget.moneyAvailable())
#  print (entertainment.transfer(500, clothingBudget))
