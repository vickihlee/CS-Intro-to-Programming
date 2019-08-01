# Vicki Lee CS110A 7/9/19 HW3

# Exercise 63: Temperature Conversion Table

# Heading
print('Celsius', 'Fahrenheit')

# Celsius and Fahrenheit temperature conversion
for num in range(1, 11):
    celsius = num * 10
    print(celsius, end='      ')
    fahrenheit = 1.8 * celsius + 32
    print(fahrenheit, end=' ')
    print('\n')