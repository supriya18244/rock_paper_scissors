"""Although the game has a lot of complexity to it, the rules to play it are pretty simple.
The game is played where players deliver hand signals that will represent the elements of the game;
rock, paper and scissors. The outcome of the game is determined by 3 simple rules:
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock."""




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

import random
hands=[paper,rock,scissors]
computer_choose=random.randint(0,2)
user_choose=int(input("Hey User! you can start choosing .which choice do you want? \n"
                  "for paper enter 0,for rock enter 1 or for scissors enter 2 : "))
print("user choose:", user_choose)
print("computer choose:",computer_choose)
if computer_choose==user_choose:
    print(f"game is draw")
if computer_choose==0 and user_choose==1:
    print(f"you loss")
if computer_choose == 0 and user_choose == 2:
    print(f"you win")
if computer_choose==1 and user_choose==0:
    print(f"you win")
if computer_choose == 2 and user_choose == 0:
    print(f"you loss")
if computer_choose==1 and user_choose==2:
    print(f"you loss")
if computer_choose==2 and user_choose==1:
    print(f"you win")






