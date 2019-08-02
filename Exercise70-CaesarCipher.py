# Vicki Lee CS110A 7/9/19 HW3

# Exercise 70: Caesar Cipher

# Ask user if encoding or decoding
message = input('Are you encoding or decoding your message?\n')

# Encoding message
if message == 'encoding':
    message = input('What is your message?\n')
    cipher = ''
    for character in message:
        if (character == 'A') or (character == 'a'):
            cipher += 'D'
        elif (character == 'B') or (character == 'b'):
            cipher += 'E'
        elif (character == 'C') or (character == 'c'):
            cipher += 'F'
        elif (character == 'D') or (character == 'd'):
            cipher += 'G'
        elif (character == 'E') or (character == 'e'):
            cipher += 'H'
        elif (character == 'F') or (character == 'f'):
            cipher += 'I'
        elif (character == 'G') or (character == 'g'):
            cipher += 'J'
        elif (character == 'H') or (character == 'h'):
            cipher += 'K'
        elif (character == 'I') or (character == 'i'):
            cipher += 'L'
        elif (character == 'J') or (character == 'J'):
            cipher += 'M'
        elif (character == 'K') or (character == 'k'):
            cipher += 'N'
        elif (character == 'L') or (character == 'l'):
            cipher += 'O'
        elif (character == 'M') or (character == 'm'):
            cipher += 'P'
        elif (character == 'N') or (character == 'n'):
            cipher += 'Q'
        elif (character == 'O') or (character == 'o'):
            cipher += 'R'
        elif (character == 'P') or (character == 'p'):
            cipher += 'S'
        elif (character == 'Q') or (character == 'q'):
            cipher += 'T'
        elif (character == 'R') or (character == 'r'):
            cipher += 'U'
        elif (character == 'S') or (character == 's'):
            cipher += 'V'
        elif (character == 'T') or (character == 't'):
            cipher += 'W'
        elif (character == 'U') or (character == 'u'):
            cipher += 'X'
        elif (character == 'V') or (character == 'v'):
            cipher += 'Y'
        elif (character == 'W') or (character == 'w'):
            cipher += 'Z'
        elif (character == 'X') or (character == 'x'):
            cipher += 'A'
        elif (character == 'Y') or (character == 'y'):
            cipher += 'B'
        elif (character == 'Z') or (character == 'z'):
            cipher += 'C'
        else:
            cipher += character
    print(cipher)

# Decoding message
else:
    message = input('What is your message?\n')
    cipher = ''
    for character in message:
        if (character == 'A') or (character == 'a'):
            cipher += 'X'
        elif (character == 'B') or (character == 'b'):
            cipher += 'Y'
        elif (character == 'C') or (character == 'c'):
            cipher += 'Z'
        elif (character == 'D') or (character == 'd'):
            cipher += 'A'
        elif (character == 'E') or (character == 'e'):
            cipher += 'B'
        elif (character == 'F') or (character == 'f'):
            cipher += 'C'
        elif (character == 'G') or (character == 'g'):
            cipher += 'D'
        elif (character == 'H') or (character == 'h'):
            cipher += 'E'
        elif (character == 'I') or (character == 'i'):
            cipher += 'F'
        elif (character == 'J') or (character == 'J'):
            cipher += 'G'
        elif (character == 'K') or (character == 'k'):
            cipher += 'H'
        elif (character == 'L') or (character == 'l'):
            cipher += 'I'
        elif (character == 'M') or (character == 'm'):
            cipher += 'J'
        elif (character == 'N') or (character == 'n'):
            cipher += 'K'
        elif (character == 'O') or (character == 'o'):
            cipher += 'L'
        elif (character == 'P') or (character == 'p'):
            cipher += 'M'
        elif (character == 'Q') or (character == 'q'):
            cipher += 'N'
        elif (character == 'R') or (character == 'r'):
            cipher += 'O'
        elif (character == 'S') or (character == 's'):
            cipher += 'P'
        elif (character == 'T') or (character == 't'):
            cipher += 'Q'
        elif (character == 'U') or (character == 'u'):
            cipher += 'R'
        elif (character == 'V') or (character == 'v'):
            cipher += 'S'
        elif (character == 'W') or (character == 'w'):
            cipher += 'T'
        elif (character == 'X') or (character == 'x'):
            cipher += 'U'
        elif (character == 'Y') or (character == 'y'):
            cipher += 'V'
        elif (character == 'Z') or (character == 'z'):
            cipher += 'W'
        else:
            cipher += character
    print(cipher)