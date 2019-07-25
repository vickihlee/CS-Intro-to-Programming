# Vicki Lee CS110A 7/19/19 Final Project

""" Milk Tea Shop: A milk tea shop offers green and black tea (same price) and
5 different toppings with different prices one can choose from (only 1 topping per drink).
The program outputs the total price of the drink.
"""

# Function for menu and cost
def cost():
    print('''\nTOPPINGS
1 - Boba
2 - Grass Jelly
3 - Lychee
4 - Mango Pudding
5 - Taro''')
    topping = input('\nPick 1 topping:\n')
    if topping == '1':
        totalcost = 4.00 + .50
    elif topping == '2':
        totalcost = 4.00 + .30
    elif topping == '3':
        totalcost = 4.00 + .25
    elif topping == '4':
        totalcost = 4.00 + .10
    elif topping == '5':
        totalcost = 4.00 + .35
    return totalcost

# Main program that gets order from user
if __name__ == '__main__':
    print("Hello, welcome to the milk tea shop! Let's start with picking your tea.\n")
    tea_list = ['green tea', 'black tea']
    for teas in tea_list:
        print(teas)
    tea_choice = input('\nWhich tea would you like?\n')
    print('\nYour total cost is $%.02f.' % cost())

"""
X menu
X user input
X loop structure (do while, while, for)
X decision structure (if else if, if else, switch)
X list or dictionary
X function
X Well documented comments
X output displaying results
X input data validation
"""