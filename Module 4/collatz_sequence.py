#Nick Wendel
#IT - 75
#9/27/19
#Collatz Sequence

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

try:
    number = int(input('Enter a number: '))
    while number != 1:
        number = collatz(int(number))
except ValueError:
    print("Please enter a valid INTEGER.")
    print()
    number = int(input('Enter a number: '))
    while number != 1:
        number = collatz(int(number))
          

    


