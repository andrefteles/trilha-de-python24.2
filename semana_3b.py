# b) Representar, por meio do uso das classes, algo do dia-a-dia de vocês,
# como a Padaria feita anteriormente.

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = 'Pending'
    
    def mark_completed(self):
        self.status = 'Completed'
    
    def __str__(self):
        return f'Task: {self.title}\nDescription: {self.description}\n\
Status: {self.status}'

class MarketItem:
    def __init__(self):
        # Use a dictionary to store items and their prices
        self.items = {
        'meat': 0,
        'frijoles': 0,
        'rice': 0,
        'fruit': 0,
        'vegetable': 0,
        'juice': 0,
        'groceries': 0,
    }   
    
    def set_price (self, item, price):
        '''Sets or updates the price of a specific item.'''
        
        if item in self.items and price >= 0:
            self.items[item] = price
        else:
            print(f'Invalid item or price for {item}.')

    def get_price(self, item):
        '''Returns the current price of a specific item.'''
        return self.items.get(item, 'Item not found.')

    def __str__(self):
        '''Display all items and their prices.'''
        return '\n'.join(f'{item}: ${price:.2f}' for item, price in self.items.items())

class myself:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        
    # my_money

title_1 = 'Buy food at the market.'
description_1 = 'I need to go to the market to buy food for the week.'

if __name__ == "__main__":
    task1 = Task(title_1, description_1)
    print(task1)
    
    task1.mark_completed()
    print(task1)