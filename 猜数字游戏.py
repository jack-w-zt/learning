import random
random_number = random.randint(1,100)
while True:
    a = int(input("请输入你要猜的数字（1~100）："))
    if a < random_number:
        print("你猜的数字太小了，请重新输入~")
    elif a > random_number:
        print("你猜的数字太大了，请重新输入~")
    else:
        print("恭喜你，猜对了！")
        break