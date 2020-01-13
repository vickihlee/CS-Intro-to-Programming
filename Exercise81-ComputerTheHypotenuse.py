# Vicki Lee CS110A 7/18/19 HW4

# Exercise 81: Compute the Hypotenuse

# Import math square root and exponent can be used
import math

# Function for getting hypotenuse
def hypotenuse(x, y):
    triangle_side3 = math.sqrt(math.pow(triangle_side1, 2)+math.pow(triangle_side2, 2))
    return triangle_side3

# Main program that gets 2 triangle sides from user
if __name__ == '__main__':
    triangle_side1 = int(input('Name one side of the triangle:\n'))
    triangle_side2 = int(input('Name one side of the triangle:\n'))
    print('The hypotenuse is %.02f.' % hypotenuse(triangle_side1, triangle_side2))