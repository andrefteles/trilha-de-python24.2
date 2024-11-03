# b) Representar, por meio do uso das classes, algo do dia-a-dia de vocês,
# como a Padaria feita anteriormente.

class Task:
    ''' Represent a task and its status. '''
    
    def __init__(self, title):
        ''' Initializes the task with a title '''
        self.title = title
        self.status = 'Pending'
    
    def display_status(self):
        ''' Displays the task status. '''
        print(f'Task "{self.title}" is currently {self.status}.')
    
    def task_completed(self):
        ''' Changes the task status to completed. '''
        self.status = 'Completed'
    
    def __str__(self):
        return f'\nTask: {self.title}\nStatus: {self.status}'

class MarketItem:
    ''' Stores products and their prices'''
    
    def __init__(self):
# TAKE A LOOK AT THE POSSIBILITY TO CREATE ANOTHER FILE WITH PRODUCTS AND PRICES INFORMATION
        # Dictionary to store products and their prices
        self.products = {
        'meat': 33.99,
        'frijoles': 5.68,
        'rice': 4.99,
        'fruit': 15.95,
        'vegetable': 4.88,
        'juice': 8.95,
        'candy': 2.99,
    }   
    
    # def get_price(self, item):
    #     '''Returns the current price of a specific item.'''
    #     return self.products.get(item, 'Item not found.')

    def __str__(self):
        '''Display all products and their prices. '''
        
        # List comprehension / generator expression
        return '\n'.join(f'{item}: R${price:.2f}'
        for item, price in self.products.items())

# Change Myself to User will be much better
class Myself:
    ''' Represents the user with name and available funds. '''
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
    
    def user_information():
        ''' Verifies and collect user information. '''
        
        try:
            # Ensure name is not empty
            user_name = input('\nWhat is your name, sir? ').strip()
            if not user_name:
                print('Name cannot be empty. Please try again. ')
                return None, None

            user_money = float(input('How much money do you have? '))
            if user_money < 0:
                print('Money cannot be negative. Please enter a valid amount.')
                return None, None
            
            return user_name, user_money
        
        except ValueError:
            print('Invalid input for money. Please enter a numeric value.')
            return None, None    
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return None, None

    def __str__(self):
        return f'Name: {self.name}. Money: R$ {self.money:.2f}'

# I need to change the class name to PurchaseCondition 
class Condition:
    ''' Manages purchasing conditions and balance updates. '''
    # def __init__(self, profit, loss):
    #     self.profit = profit
    #     self.loss = loss        
    
    # I need to try other approach to use the function above.
    @staticmethod

    def possibility_to_buy(user_money, total):
        
        # I'm having a problem with the total increasing when the
        # user doesn't have enough funds to buy. I need to verify
        # it here or bellow.
        if total > user_money:
            print('you do not have enough funds to complete this purchase.')
        else:
            user_money -= total
            print(f'Remaining balance: R$ {user_money:.2f}')

if __name__ == '__main__':

    # Defining task
    title_1 = 'Buy food at the market.'

    # Task demonstration
    task1 = Task(title_1)
    print(task1)

    # MarketItem demonstration
    market_products = MarketItem()
    print("\nMarket products and prices:")
    print(market_products)


    # User information collection
    user_name, user_money = Myself.user_information()
    while user_name is None or user_money is None:
        user_name, user_money = Myself.user_information()

    if user_name is not None and user_money is not None:
        user = Myself(user_name, user_money)
        print("\nUser information:")
        print(f'{user}')

    market = MarketItem()
    total = 0

# Select things to buy
while True:
    user_buying = input('\nWhat would you like to buy? ').strip().lower()
    
    # Check if the product is available
    if user_buying in market.products:
        price = market.products[user_buying]
        print(f'You bought {user_buying} for R${price:.2f} \n')
        total += price

        # Check if the user can continue shopping
        Condition.possibility_to_buy(user_money, total)
        
        user_buying_more = input(
        'Would you like to buy more products? (yes/no) ').strip().lower()
        
        if user_buying_more == 'no':
            break
        # elif user_buying_more == 'no':
        #     break
    else:
        print('You are buying the wrong products!')
        continue

total_spend = total
print(f'\nTotal spend: R${total_spend:.2f}')

task1.task_completed()

# This will now print: Task: Buy groceries at the market. Status: Completed
print(task1)