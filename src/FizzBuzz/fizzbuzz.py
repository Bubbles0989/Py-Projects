

def fizzbuzz(x):
    if x > 100:
        return 'Numbers between 1 and 100 please.'
    elif x < 1:
        return 'Numbers between 1 and 100 please.'
    
    remainder_of_3 = x % 3
    remainder_of_5 = x % 5

    if remainder_of_3 == 0 and remainder_of_5 == 0:
        return 'fizzbuzz'
    elif remainder_of_5 == 0:
        return 'buzz'
    elif remainder_of_3 == 0:
        return 'fizz'
    else:
        return x


if __name__ == "__main__":
    print("Fizzbuzz~ <3\n")

    userInput = int(input("Give me a number between 1 and 100 please~ >> "))

    print(fizzbuzz(userInput))

    # for number in range(0, 101):
    #     print(fizzbuzz(number))   