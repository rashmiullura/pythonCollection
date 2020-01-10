# Consecutive prime sum
#
# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# ------------------------------------------------------------------------------

# idea:
# * implement function to compute all primes up to a certain limit
# * for each elem (prime) inside that list, check if a possible, consecutive sublist can be added up to that prime ->
# return the longest chain for each prime; sometimes maybe empty list
# * check which prime has the longest list

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

# reuse code from previous solution
# TODO maybe consider to use a prime-generator, which is proven and tested; see problem041
def getPrimesUntilLimit(limit):
    from ProjectEuler.problem668_numpy import sieveEras  # works, but just after commenting lots of code inside that file
    primes = sieveEras(limit, False) # this is also a mistake in the second parameter
    #print(len(primes), ":", primes)  # 78,498 for 10 ** 6 - which is correct

    return primes

# ------------------------------------------------------------------------------

def findLongestChainForPrime(target, primes):

    # maybe move this outside to save additional computation
    subList = [elem for elem in primes if elem <= target]
    print(subList)

    # check all sublists of that list (starting with the first element)
    for elem in subList:
        currentList = [item for item in subList if item >= elem]

        sum = 0
        count = 0
        resultSummands = []
        for elem in currentList: #shadowing, but idc
            sum += elem
            count += 1
            resultSummands.append(elem)
            if sum >= target:
                print("sum bigger-equal target")
                break
        if sum == target:
            print("found one chain:", count)
            break
        if sum >= target:
            print("just too big :/")
            resultSummands = []
            break

    if len(resultSummands) > 0:
        print("we have a chain:", resultSummands)

    return resultSummands

# ------------------------------------------------------------------------------

# proper unit-test

import unittest

#@unittest.skip("unwanted for now")
class Testcase(unittest.TestCase):

    def test_primeGen(self):
        import time
        expectedOutput = 78498
        startTime = time.time()
        primes = getPrimesUntilLimit(10 ** 6)
        computedOutput = len(primes)
        timeTakenToCompute = time.time() - startTime
        self.assertEqual(expectedOutput, computedOutput)
        print("computation of primes up to 10 ** 6 took", timeTakenToCompute, "s")
        print("last prime:", primes[-1])

# ---- here comes the execution of the unit-tests ----
# if __name__ == '__main__':
#     unittest.main()

# ------------------------------------------------------------------------------

# test
print("#############################################")
limit = 10 ** 3
primes = getPrimesUntilLimit(limit)
print("primes until", limit, ":", primes)
chain = findLongestChainForPrime(41, primes)
print("chain for 41:", chain)
