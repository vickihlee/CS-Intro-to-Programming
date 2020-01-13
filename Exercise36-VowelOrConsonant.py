# Vicki Lee CS110A 7/9/19 HW3

# Exercise 36: Vowel or Consonant

# Input of alphabet letter
letter = input('Name a letter of the alphabet.\n') #works

# Determine if vowel, y, or other
if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'): #works if != or > or #. not for =.
    print('The entered letter is a vowel.')
elif letter == 'y':
    print('Sometimes y is a vowel, and sometimes y is a consonant.')
else:
    print('The letter is a consonant.')