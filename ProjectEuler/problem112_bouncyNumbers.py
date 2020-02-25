# Bouncy numbers
#
# Problem 112
#
# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
# for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below
# one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first
# reaches 50% is 538.
#
# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy
# numbers is equal to 90%.
#
# Find the least number for which the proportion of bouncy numbers is exactly 99%.

# ------------------------------------------------------------------------------

# idea:
# TODO

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

import enum
class Type(enum.Enum):
    ''' Enum to determine which type a number is. '''
    Increasing = 0
    Decreasing = 1
    Bouncy = 2

# ------------------------------------------------------------------------------

class Direction(enum.Enum):
    ''' Enum to determine which type a number is. '''
    Equal = 0
    Up = 1
    Down = 2
# ------------------------------------------------------------------------------

def determineType(number):
    ''' Returns Increasing, Decreasing or Bouncy :) '''

    # parsing direction is left-to-right

    rising = True
    numberStr = str(number)
    lastValue = int(numberStr[0]) # will have at least one digit
    for elem in numberStr[1:]:
        currentValue = int(elem)
        if currentValue <= lastValue:
            rising = False
            break

    if rising:
        return Type.Increasing

    # TODO

    return Type.Bouncy

# ------------------------------------------------------------------------------

# add unit-tests

# ------------------------------------------------------------------------------

numberToTest = 134468
result = determineType(numberToTest)
print(numberToTest, "is", result)