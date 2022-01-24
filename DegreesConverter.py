while True:
    print("Enter degrees by Celsius or Fahrenheit or Kelvin, for example, '23 C' or '23 F' or '23 K':")

    degrees = input()

    try:
        num, letter = degrees.split(' ')
    except Exception:
        print('Invalid input')

    try:
        if letter == 'C' or letter == 'c':
            CF = round(float(num) * 1.8 + 32, 2)
            CK = round(float(num) + 273.15, 2)
            print('Conversion result: ' + num + '°С = ' + str(CF) + '°F')
            print('Conversion result: ' + num + '°C = ' + str(CK) + '°K')
        elif letter == 'F' or letter == 'f':
            FC = round((float(num) - 32) / 9 * 5, 2)
            FK = round((float(num) - 32) / 9 * 5 + 273.15, 2)
            print('Conversion result: ' + num + '°F = ' + str(FC) + '°С')
            print('Conversion result: ' + num + '°F = ' + str(FK) + '°K')
        elif letter == 'K' or letter == 'k':
            KC = round(float(num) - 273.15, 2)
            KF = round((float(num) - 273.15) * 1.8 + 32, 2)
            print('Conversion result: ' + num + '°K = ' + str(KC) + '°С')
            print('Conversion result: ' + num + '°K = ' + str(KF) + '°F')
        else:
            print('Invalid second argument')
    except Exception:
        print('Invalid first argument')
