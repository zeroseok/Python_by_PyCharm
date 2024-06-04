# Setting a Study Date
# We created a coding study group.
# We decided to gather four times a month, three times online and one time offline.
# Write a program that sets the date for the offline meeting that meets the conditions.

# condition
# 1. Pick a date at random.
# 2. Select a date only until the 28th because the number of days per month is different
# 3. Exclude the study from 1st to 3rd of every month because you need to prepare for it.

from random import *
date = randint(4,28) # Randomize from the numbers 4 to 28.
print("The date of the offline study meeting was selected as the " + str(date) + "th of every month.")
