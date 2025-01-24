import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
visual = [rock, paper, scissors]
comp = random.randint(0, 2)
user = int(input('''0. Rock
1. Paper
2. Scissor
Enter choice: '''))
print(f"\nComputer chose: \n{visual[comp]}")
print(f"You chose: \n{visual[user]}")
result = user - comp
if result == 0:
    print("It's a draw")
if result == 1 or result == -2:
    print("You Win")
if result == 2 or result == -1:
    print("Computer wins")
"""
COMP	    USER	COMP – USER	    USER – COMP	    WINS	USER	COMP
ROCK 0	    PAPER 1	    -1	            1	        USER	1	
ROCK 0	    SCISSOR 2	-2	            2	        COMP		     2
PAPER 1	    ROCK 0	     1	           -1	        COMP		    -1
PAPER 1	    SCISSOR 2	-1	            1	        USER	1	
SCISSOR 2	ROCK 0	     2	           -2	        USER   -2	
SCISSOR 2	PAPER 1	     1	           -1	        COMP	        -1

"""
