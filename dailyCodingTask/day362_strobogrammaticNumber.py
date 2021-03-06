# This problem was asked by Twitter.
#
# A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees.
# For example, 16891 is strobogrammatic.
#
# Create a program that finds all strobogrammatic numbers with N digits.

# ------------------------------------------------------------------------------

# idea: if string is of length 0 or 1: is strobo; else: compare the first and last character for rotation-awareness;
# then apply the function to the inner string
#
# 1 is rotatable (is this a word?) to 1
# 2 to 5? (i would say yes, but this depends on the type of glyphs which are used; is a detail ..)
# 6 to 9
# 8 to itself
# 3, 4, 7 are fitting to nothing ... so if first/last is one of those, then discard

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

# added also the switched case to this list, so the code is simpler
fittingPairs = [(1, 1),
                (2, 5),
                (5, 2), # remove if 5 =/= 2
                (6, 9),
                (8, 8), # remove if 5 =/= 2
                (9, 6),
                ]

def isStroboGrammmatic(number):
    # check if first and last as pair are inside the fitting pairs-LUT; if yes,
    # then apply the function to the inner part (without head and tail) and use that return-value for return.
    # Attention: number should be an integer

    strNumber = str(number)
    #print(f"#### isStroboGrammmatic for {strNumber} ####") # the new f-string :)

    if len(strNumber) < 2:
        # strings of length 0 or 1 are always strobo
        return True

    # get the head and tail and convert them back to int
    first = int(strNumber[:1])
    last = int(strNumber[-1:])
    #print(first, last) # todo remove

    middle = strNumber[1:-1]
    #print("middle:", middle) # todo remove

    headAndTailAreStrobo = False
    for a,b in fittingPairs:
        if a == first and b == last:
            headAndTailAreStrobo = isStroboGrammmatic(int(middle))

    return headAndTailAreStrobo

# ------------------------------------------------------------------------------

def getAllStroboNumbersWithNDigits(n):
    # sanity check
    if n < 1:
        return []

    # generate the range
    start = 10 ** (n-1)
    end = 10 ** n
    print("range:", start, end) # todo remove

    resultList = []
    for number in range(start, end):
        if isStroboGrammmatic(number):
            print("number", number, "is strobogrammatic ..")
            resultList.append(number)

    return resultList

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_givenExample0(self):
        number = 16891
        expectedOutput = True
        computedOutput = isStroboGrammmatic(number)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExample1(self):
        number = 123
        expectedOutput = False
        computedOutput = isStroboGrammmatic(number)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExample2(self):
        number = 4
        expectedOutput = True
        computedOutput = isStroboGrammmatic(number)
        self.assertEqual(expectedOutput, computedOutput)

    def test_givenExample3(self):
        number = 1531
        expectedOutput = False
        computedOutput = isStroboGrammmatic(number)
        self.assertEqual(expectedOutput, computedOutput)

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------

#print(getAllStroboNumbersWithNDigits(4))
