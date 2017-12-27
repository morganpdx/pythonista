# Example of the collatz sequence

tries = 0

def collatz(number):
    # Determine if even or odd
    try:
        if number % 2 == 0:
            result = number // 2
            print(str(result))
            return result
        else:
            result = 3 * number + 1
            print(str(result))
            return result

    except:
        print('Please enter a valid integer.')

print('Collatz sequence: Enter a number and determine how many times it takes to get to 1.')
print('Enter a number:')

try:
    currentNumber = int(input())

    while currentNumber <> 1:
        currentNumber = collatz(currentNumber)
        tries += 1

    print('Got to 1 in ' + str(tries) + ' tries!')

except:
    print('Please enter a valid integer.')

