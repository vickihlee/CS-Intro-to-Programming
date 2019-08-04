# Vicki Lee CS110A 7/18/19 HW4

# Exercise 82: Taxi Fare

# Function for getting total fare
def fare(distance_traveled):
    distance_meters = distance_traveled * 1000
    totalfare = base_fare + (distance_meters / 140 * .25)
    return totalfare

# Main program that gets fare prices and distance from user
if __name__ == '__main__':
    base_fare = float(input('What is the base fare?\n'))
    extra_fare = float(input('What is the extra fare?\n'))
    distance_traveled = float(input('What is the distance traveled in kilometers?\n'))
    print('The total fare is $%.02f.' % fare(distance_traveled))