import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# =======================================================================
# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# >>>
#   Ans: 11
#   The smallest number I could have seen is 5, the largest is 20.
# =======================================================================
# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# >>>
#   Ans: 7
#   The smallest number I could see is 3, and the largest is 9
#   Line 2 could not produce a 4
# =======================================================================
# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# >>>
#   Ans: 5.082733953117112
#   The smallest number I could see is 2.5, and the largest is 5.5
# =======================================================================
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 101))
