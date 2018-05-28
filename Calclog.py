import math
import random
import numpy as np
import matplotlib.pyplot as plt


def risk(lose_rate, pay_rate, total_money, win_rate):
    """
    :param lose_rate: rate of lose
    :param pay_rate: rate of total money you risk
    :param total_money: total money you have
    :param win_rate: rate of money you win
    :return: total money after this term
    """
    lose_rate_round = round(lose_rate, 2)
    if lose_rate_round >= 1 or pay_rate > 1 or win_rate > 1:
        print('lose or pay rate error')
        return 0
    if total_money <= 0:
        print("you have no money")
        return 0
    randnum = random.randint(0, 100)
    if randnum >= 100 * lose_rate_round:  # 成功
        return total_money * (1 - pay_rate) + total_money * pay_rate * (1 + win_rate)
    else:
        return total_money * (1 - pay_rate)


def try_bet(times):
    ans = []
    if times <= 1:
        return ans
    for i in range(100000):
        money = 1
        for j in range(times):
            if money == 0:
                break
            money = risk(loserate, payrate, money, winrate)
        ans.append(money)
    return np.array(ans, dtype=np.float32)



if __name__ == "__main__":
    mymoney = 82.0
    target = 2000.0
    baserate = 0.4
    loserate = 0.2
    payrate = 0.5
    winrate = 0.4
    # riskrate =
    # print("you need to win ",int(math.log(target/mymoney, 1 + baserate/2)), " times")
    data = try_bet(10)
    fig  = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(data, bins=5)
    plt.title("win rate distribution")
    plt.xlabel('win rate')
    plt.ylabel('count')
    plt.show()
    # x = risk(loserate,payrate,10,0.4)
    # print(x)

