# We created a coding study group.
# It was decided to gather four times a month, three times online and one time offline.
# Write a program that sets a date for an offline meeting that satisfies the conditions.

# conditions
# 1. Pick a date at random.
# 2. Since the number of days in each month is different, set it to 28 days.
# 3. Exclude 1 to 3 days every month because you have to study.

from random import *
date = randint(4,28) # Pick a random number from 4 to 28
print("The offline study meeting date is the " + str(date) + "th of every month.")