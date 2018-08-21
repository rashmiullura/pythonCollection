# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
# the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
# primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# ------------------------------------------------------------------------------
import unittest
# ------------------------------------------------------------------------------

def isPrime(input):
    upperLimit = input // 2 + 1
    for x in range(2, upperLimit):
        if input % x == 0:
            return False
    # else we have a prime if we reached this
    return True

# ------------------------------------------------------------------------------

def getPrime():
    currentNumber = 1
    while True:
        currentNumber += 1
        if isPrime(currentNumber):
            yield currentNumber

# ------------------------------------------------------------------------------

def getPrimeNumber(number):
    primes = getPrime()
    for i in range(1, number):
        primes.__next__()
    return primes.__next__()

# ------------------------------------------------------------------------------

class Testcase(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(True, isPrime(2))
        self.assertEqual(True, isPrime(3))
        self.assertEqual(False, isPrime(6))
        self.assertEqual(True, isPrime(7))
        self.assertEqual(False, isPrime(16))
        self.assertEqual(False, isPrime(25))
        self.assertEqual(True, isPrime(29))
        self.assertEqual(False, isPrime(87))
        self.assertEqual(True, isPrime(89))

    def test_getPrimeNumber(self):
        self.assertEqual(2, getPrimeNumber(1))
        self.assertEqual(7, getPrimeNumber(4)) # shuffled order
        self.assertEqual(3, getPrimeNumber(2))
        self.assertEqual(13, getPrimeNumber(6))

# ------------------------------------------------------------------------------

# ---- here comes the execution of the unit-tests ----
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------------
