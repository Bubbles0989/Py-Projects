
def romanNumeralConverter(x):
    if x < 0: return "Can't do less than 0"
    elif x == 0: return str(x)[:-1]
    elif x >=100 : return "C" + romanNumeralConverter(x - 100)
    elif x >=50 : return "L" + romanNumeralConverter(x - 50)
    elif x >=10 : return "X" + romanNumeralConverter(x - 10)
    elif x >=9 : return "IX" + romanNumeralConverter(x - 9)
    elif x >=5 : return "V" + romanNumeralConverter(x - 5)
    elif x >=4 : return "IV" + romanNumeralConverter(x - 4)
    elif x >=1 : return "I" + romanNumeralConverter(x - 1)


if __name__ == "__main__":
    print("Roman Numerals Converter")
    
    while True:
        try:
            userInput = int(input("\nGive me a positive number, please >> "))
            print(romanNumeralConverter(userInput))

        except ValueError:
            print("Thats not a number... ")

    