# Implementing the Health Potion Project

# The import is highlighted because it is a reserved word in the Python language.
# Reserved words are generally highlighted by editors to show that they are special.
# Reserved words cannot be used as variable names.
# Import statments need to be at the beginning of each python file since Python
# executes from top to bottom, left to right.
import random

health = 50

# randint is a function in the random module.
# Functions are called using parentheses().
# When you call a function, you pass in parameters.
potion_health = random.randint(25, 50)
print(potion_health)
