salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев


def living(sl, sp, m, inc):
    n_n = sp - sl
    for i in range(1,m):
        sp *= (1+inc)
        n_n += sp - sl
    return n_n


need_money = living(salary, spend, months, increase)


print(round(need_money))
