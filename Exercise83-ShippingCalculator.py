# Vicki Lee CS110A 7/18/19 HW4

# Exercise 83: Shipping Calculator

# Function for getting total shipping charge
def charge(num_items):
    additional_items = num_items - 1
    if num_items == 1:
        shippingcharge = 10.95
    elif num_items > 1:
        shippingcharge = 10.95 + (additional_items * 2.95)
    return shippingcharge

# Main program that gets number of items from user
if __name__ == '__main__':
    num_items = int(input('How many items do you have?\n'))
    print('Your shipping charge is $%.02f.' % charge(num_items))