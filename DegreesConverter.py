print("Enter degrees by Celsius or Fahrenheit, for example, '23 C' or '23 F':")

input = input()

try:
    num, letter = input.split(' ')
except Exception:
    print('Invalid input')

try:
    if letter == 'C' or letter == 'c':
        CF = round(float(num) * 1.8 + 32, 2)
        print('Conversion result: ' + num + '°С = ' + str(CF) + '°F')
    elif letter == 'F' or letter == 'f':
        FC = round((float(num) - 32) / 9 * 5, 2)
        print('Conversion result: ' + num + '°F = ' + str(FC) + '°С')
    else:
        print('Invalid second argument')
except Exception:
    print('Invalid first argument')