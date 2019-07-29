#Vicki Lee CS110A 6/30/19 HW2

#Exercise 4: Tax and Tip

#Input of cost of meal
meal_cost = float(input('What is the cost of your meal?\n'))

#Tax, tip, and total cost of meal
tax = meal_cost * .085
tip = meal_cost * .18
total_cost = meal_cost + tax + tip

print'Tax at 8.5% is:', '$%.02f' % tax
print'Tip at 18% is:', '$%.02f' % tip
print'Total cost is:', '$%.02f' % total_cost