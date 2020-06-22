import random

player = int( input("please input stone（1）/ scissors（2）/ paper（3）："))
computer = random.randint(1, 3)
print("you are：", player, "-", "computer is：", computer)
if (player == 1 and computer == 2) or \
        (player == 2 and computer == 3) or \
        (player == 3 and computer == 1):
    print(" winner winner, chicken dinner!")
elif player == computer:
    print("not bad,try again!")
else:
    print("the computer is smarter than you~")
