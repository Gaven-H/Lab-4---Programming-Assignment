import random

num_to_guess = random.randint(1,15)

hangman_states = [

"""
________
|      |
|
|
|
|
===========
""",
"""
________
|      |
|      0
|
|
|
===========
""",
"""
________
|      |
|      0
|      |
|
|
===========
""",
"""
________
|      |
|      0
|     /|
|
|
===========
""",
"""
________
|      |
|      0
|     /|\\
|
|
===========
""",
"""
________
|      |
|      0
|     /|\\
|     /
|
===========
""",
"""
________
|      |
|      0
|     /|\\
|     / \\
|
===========
"""
]

wrong_guess_counter = 0

game_state = True

print ("Guess the number including and between 1-15!")
print ("Each wrong guess takes you one step closer to avoid an untimely end...")
print ("Worry not, you will be given mysterious assistance from beyond!")