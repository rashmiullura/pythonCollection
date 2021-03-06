# Digit factorials
#
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# ------------------------------------------------------------------------------
# idea:
# * a function to compute the factorial (maybe with dictionary for caching) - not really needed, because just 0 to 9
# * if one of the factorials is bigger than the wanted sum, then it can be skipped immediately, or?
# * what is the boundary? how to know to stop?
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

class FactorialChecker:

    # class attribute
    factDict = {}

    def __init__(self):

        # prepare the factorial dictionary
        self.factDict[0] = 1 # by definition
        currentFact = 1
        for elem in range(1, 10):
            # compute the next fact
            currentFact *= elem
            # insert into dict
            self.factDict[elem] = currentFact

        print("current dictionary:", self.factDict) # todom remove

    # ----------------------------

    def computeResultsForRange(self, lowerLimit, upperLimit):
        ''' Used to run the check given by the task:
        is the sum of the factorial of the digits equal to the number itself?'''

        print("check numbers from", lowerLimit, "to", upperLimit)
        result = 0
        for number in range(lowerLimit, upperLimit + 1):
            if self.isDigitFactorialNumber(number):
                print("hit:", number)
                result += number

        print("... done ...")
        print("result is:", result)

    # ----------------------------

    def isDigitFactorialNumber(self, number):
        # convert to digits
        digits = [int(digit) for digit in str(number)]
        # excluded by definition of the task, because not a sum
        if len(digits) < 2:
            return False

        # compute the sum of the factorials of the digits
        summed = sum([self.factDict[digit] for digit in digits])
        # are the equal?
        return summed == number

# ------------------------------------------------------------------------------

factChecker = FactorialChecker()

# print("145?", foo.isDigitFactorialNumber(145))
# print("123?", foo.isDigitFactorialNumber(123))

factChecker.computeResultsForRange(0, 10000000)

# ------------------------------------------------------------------------------
# current dictionary: {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
# check numbers from 0 to 10000000
# hit: 145
# hit: 40585
# ... done ...
# result is: 40730
# ------------------------------------------------------------------------------

# Congratulations, the answer you gave to problem 34 is correct.
#
# You are the 88179th person to have solved this problem.
#
# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved so far is 20%.

# ------------------------------------------------------------------------------

# interesting note: those numbers are called Factorion!
#
# see: http://mathworld.wolfram.com/Factorion.html
#  A factorion is an integer which is equal to the sum of factorials of its digits. There are exactly four such numbers:
# 1	=	1!
# (1)
# 2	=	2!
# (2)
# 145	=	1!+4!+5!
# (3)
# 40585	=	4!+0!+5!+8!+5!
# (4)
#
# (OEIS A014080; Gardner 1978, Madachy 1979, Pickover 1995). Obviously, the factorion of an n-digit number cannot exceed n·9!.
