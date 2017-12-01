"""
猜数字游戏
设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，
每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，
结束游戏并告知正确答案。
"""

import random


class GuessNumGame:
    def __init__(self, min_num, max_num, choice):
        """

        :param min_num: 最小值
        :param max_num: 最大值
        :param choice: 猜测次数
        """

        self.min_num = min_num
        self.max_num = max_num
        self.choice = choice
        self.target = random.randint(min_num, max_num)

    def guess(self):
        """
        猜字方法

        :return:
        """

        choice = self.choice

        while choice > 0:

            try:
                num = int(input("请输入猜测数字："))
            except ValueError as e:
                print("请输入有效数字")
                continue

            choice -= 1

            if self.target == num:
                print("恭喜你，猜中了")
                break
            elif self.target < num:
                print("猜大了，你还有%d次机会" % choice)
            else:
                print("猜小了，你还有%d次机会" % choice)
        else:
            print("抱歉，%d次机会都用完了，差一点就猜中了，正确答案是%d" % (self.choice, self.target))


if __name__ == '__main__':
    game = GuessNumGame(1, 100, 5)
    # print(game.target)
    game.guess()
