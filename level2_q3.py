number = int(input("Please enter a number between 0-35: "))
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

if number <= 9:
    print(number)
elif number <= 35:
    index = number - 10
    print(letters[index])