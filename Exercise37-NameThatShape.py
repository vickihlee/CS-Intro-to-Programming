# Vicki Lee CS110A 7/9/19 HW3

# Exercise 37: Name that Shape

# Input of number of sides
sides = int(input('Give a number of sides for a shape.\n'))

# Output shape
if sides == 3:
    print('triangle')
elif sides == 4:
    print('square')
elif sides == 5:
    print('pentagon')
elif sides == 6:
    print('hexagon')
elif sides == 7:
    print('heptagon')
elif sides == 8:
    print('octagon')
elif sides == 9:
    print('enneagon')
elif sides == 10:
    print('decagon')
else:
    print('The number is outside the range for shapes.')