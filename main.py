import budget
    #variable constant
DEPOSIT = 1
WITHDRAW = 2
TRANSFER = 3
BALANCE = 4
FOOD = 1
CLOTHING = 2
ENTERTAINMENT = 3
YES = 1
NO = 2
QUIT = 5
def main():
    choice = category_choice()
    method = category_method()
    start_bal = float(input('Enter your starting balance: '))
    food = budget.Budget('FOOD', start_bal)
    clothing = budget.Budget('CLOTHING', start_bal)
    entertainment = budget.Budget('ENTERTAINMENT', start_bal)
    while choice != QUIT:
        if choice == 1 and method == 1 :
            food.deposit(deposit())
            print(f'you currently have ${food.getbalance()} for food budget')
        elif choice == 1 and method == 2:
            food.withdraw(withdraw())
            print(f'you currently have ${food.getbalance()} for food budget')
        elif choice == 1 and method == 3:
            print('__________________')
            print('Enter clothing or entertainment to transfer from food')
            trans = input('clothing/entertainment: ')
            if trans.lower() == clothing:
                amount= float(input('enter amount to transfer: '))
                food.transfer(amount, clothing)
            else:
                amount= float(input('enter amount to transfer: '))
                food.transfer(amount, entertainment)
            print(f'you currently have ${food.getbalance()} for food budget')
        elif choice == 1 and method == 4:
            print(f'you currently have ${food.getbalance()} for food budget')
        elif choice == 2 and method == 1:
            clothing.deposit(deposit())
            print(f'you currently have ${clothing.getbalance()} for clothing budget')
        elif choice == 2 and method == 2:
            clothing.withdraw(withdraw())
            print(f'you currently have ${clothing.getbalance()} for clothing budget')
        elif choice == 2 and method == 3:
            print('__________________')
            print('Enter food or entertainment to transfer amount from clothing')
            trans = input('food/entertainment: ')
            if trans.lower() == food:
                amount= float(input('enter amount to transfer: '))
                clothing.transfer(amount, food)
            else:
                amount= float(input('enter amount to transfer: '))
                clothing.transfer(amount, entertainment) 
            print(f'you currently have ${clothing.getbalance()} for clothing budget')   
        elif choice == 2 and method == 4:
            #display balance
            print(f'you currently have ${clothing.getbalance()} for clothing budget')
        elif choice == 3 and method == 1:
            entertainment.deposit(deposit())
            print(f'you currently have ${entertainment.getbalance()} for entertainment budget')
        elif choice == 3 and method == 2:
            entertainment.withdraw(withdraw())
            print(f'you currently have ${entertainment.getbalance()} for entertainment budget')
        elif choice == 3 and method == 3:
            print('__________________')
            print('Enter food or clothing to transfer amount from entertainment')
            trans = input('food/clothing: ')
            if trans.lower() == clothing:
                amount= float(input('enter amount to transfer: '))
                food.transfer(amount, clothing)
            else:
                amount= float(input('enter amount to transfer: '))
                entertainment.transfer(amount, food)
            print(f'you currently have ${entertainment.getbalance()} for entertainment budget')
        elif choice == 3 and method == 4:
            print(f'you currently have ${entertainment.getbalance()} for entertainment budget')   
        print('Do YOU WANT TO PERFORM ANOTHER TRANSACTION')
        another = Another_Trans()
        if another == 1:    
            choice = category_choice()
            method = category_method()
        else:
            choice = QUIT  
def Another_Trans():
    print('________________')
    print('1. YES')
    print('2. NO')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < YES or choice > NO:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice          
def category_choice():    
    print('________________')
    print('1. food')
    print('2. clothing')
    print('3. entertainment')

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < FOOD or choice > ENTERTAINMENT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice                  
def category_method():
    print('________________')
    print('1. DEPOSIT')
    print('2. WITHDRAW')
    print('3. TRANSFER')
    print('4. BALANCE')

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < DEPOSIT or choice > BALANCE:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice              
    print()

def deposit():
    amount = float(input(f'how much do you want to deposit in this budget: '))
    return amount
def withdraw():
    amount = float(input(f'how much do you want to withdraw in this budget: '))
    return amount
main()    