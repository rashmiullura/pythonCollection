# Reciprocal cycles
#
# Problem 26
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
# 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit
# recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# ------------------------------------------------------------------------------
# idea:
# * first idea was to convert each broken number (gebrochene zahl?) to a string and then trying to find the smallest
# repeating pattern. search led to a quite short idea via regex. but this would have not been my solution. next were some
# ideas about finding periodic strings (with python). nice ...
#
# and then i found this: https://www.arndt-bruenner.de/mathe/scripts/periodenlaenge.htm
# "Die Periode eines Bruchs mit dem Nenner n kann höchstens n-1 Stellen haben, denn spätestens beim n-ten Rest muß
# sich ein bereits dagewesener Rest wiederholen."

# ------------------------------------------------------------------------------
# implementation
# ------------------------------------------------------------------------------

def driverForTask():

    result = 1

    print("result:", result)

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    driverForTask()

# ------------------------------------------------------------------------------
