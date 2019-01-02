# This problem was asked by Facebook.
#
# Given a number in Roman numeral format, convert it to decimal.
#
# The values of Roman numerals are as follows:
#
# {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }
#
# In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
#
# For the input XIV, for instance, you should return 14.

# ------------------------------------------------------------------------------

import unittest

# ------------------------------------------------------------------------------

conversionTable = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

# ------------------------------------------------------------------------------

def convertRomantToDecimal(input):
    # first: convert to upp-case
    romanNumber = str(input).upper()
    print("romanNumber: ", romanNumber)

    # check if it only consists of the allowed letters
    # TODO

    # convert the given input
    decimalValue = 0
    for digit in romanNumber:
        print("\t", conversionTable[digit])
        decimalValue += conversionTable[digit]

    return decimalValue

# ------------------------------------------------------------------------------
# proper unit-test
class Testcase(unittest.TestCase):
    def test_simpleNumbers(self):
        self.assertEqual(1, convertRomantToDecimal("I"))
        self.assertEqual(2, convertRomantToDecimal("II"))
        self.assertEqual(3, convertRomantToDecimal("III"))
        self.assertEqual(1, convertRomantToDecimal("i"))
        self.assertEqual(2, convertRomantToDecimal("ii"))
        self.assertEqual(3, convertRomantToDecimal("iii"))

        self.assertEqual(1666, convertRomantToDecimal("MDCLXVI"))


# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()
