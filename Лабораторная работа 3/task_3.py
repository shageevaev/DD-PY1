money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0


def living(m_c, sl, sp, inc):
    count = 0
    m_c_sp = m_c - sp * (1 + inc * count)
    while m_c_sp > 0:
        m_c = m_c_sp + sl
        count += 1
        m_c_sp = m_c - sp * (1 + inc * count)
    return count

month = living(money_capital, salary, spend, increase)


print(month)
