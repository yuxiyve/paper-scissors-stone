import random

player = int( input("请输入石头（1）/ 剪刀（2）/ 布（3）："))
computer = random.randint(1, 3)
print("玩家的拳头是：", player, "-", "电脑的拳头是：", computer)
if (player == 1 and computer == 2) or \
        (player == 2 and computer == 3) or \
        (player == 3 and computer == 1):
    print(" winner winner chicken dinner!")
elif player == computer:
    print("not bad,try again!")
else:
    print("you are stupid~")