# 收益计算方法1 : 计算一年的本金+收益 = 本金 * (1+利率)
def calincome1(amt, rate):
    '''收益计算方法1 : 计算一年的本金+收益 = 本金 * (1+利率)'''
    income = amt * (1 + rate)
    return round(income)


# 收益计算方法2 : 计算一年的利息收益 = 本金 * 利率
def calincome2(amt, rate):
    '''收益计算方法2 : 计算一年的利息收益 = 本金 * 利率'''
    income = amt * rate
    return round(income)


# A方式2019年开始的资金池计算方法
def fundA_cal(fund, rate1, amt4, rate2, lifecost):
    '''# A方式2019年开始的资金池计算方法'''
    tempA = calincome1(fund, rate1)
    tempB = calincome2(amt4, rate2)
    fundA = tempA + tempB - amt4 - lifecost
    return round(fundA)


# A方式计算资金池, 数年后
def fundA_cal_years(fundfirst, rate1, amt4, rate2, years, fundlist, lifecost):
    '''A方式计算资金池, 数年后
        入参:
        1、fundfirst:第一年资金池
        2、rate1:年化利率
        3、amt4:每年还贷金额
        4、rate2:半年年化利率
        5、years > 0 :投资年份
        6、fundlist :记录用list
        7、lifecost: 每年额外开支
    '''
    leftyears = years
    if (leftyears > 0):
        fundA = fundA_cal(fundfirst, rate1, amt4, rate2, lifecost)
        fundlist.append(fundA)
        leftyears = leftyears - 1
        fundA_cal_years(fundA, rate1, amt4, rate2, leftyears, fundlist, lifecost)


# B方式计算收益+利息:入参=本金、年份、利率
def fundB_cal(fund, years, years2, rate, fundlist, lifecost):
    '''
    :param fund: 本金
    :param years: 投资年份
    :param years2 : 需要计算额外开支的年数
    :param rate: 年化利率
    :param fundlist: 记录用list
    :param lifecost: 每年额外开支
    :return: None
    '''

    leftyears = years
    if (leftyears >= years2):
        fundnextyear = round(fund * (1 + rate))
        fundlist.append(fundnextyear)
        leftyears = leftyears - 1
        fundB_cal(fundnextyear, leftyears, years2, rate, fundlist, lifecost)
    elif (leftyears > 0):
        fundnextyear = round((fund - lifecost) * (1 + rate))
        fundlist.append(fundnextyear)
        leftyears = leftyears - 1
        fundB_cal(fundnextyear, leftyears, years2, rate, fundlist, lifecost)


def loadpayperyear(firstpay):
    '''
    :param firstpay:首付金额金额
    :return: 每年还贷数
    '''
    if firstpay == 200:
        payperyear = (2.63 - 0.6) * 12
    if firstpay == 250:
        payperyear = (2.368 - 0.6) * 12
    if firstpay == 300:
        payperyear = (2.1 - 0.6) * 12
    if firstpay == 400:
        payperyear = (1.57 - 0.6) * 12
    if firstpay == 500:
        payperyear = (1.05 - 0.6) * 12
    return payperyear


def loadpayperyear2(firstpay):
    '''
    计算只供金碧的每年还贷
    :param firstpay:首付金额金额
    :return: 每年还贷数
    '''
    if firstpay == 150:
        payperyear = (1.837 - 0.6) * 12
    if firstpay == 200:
        payperyear = (1.57 - 0.6) * 12
    if firstpay == 250:
        payperyear = (1.3086 - 0.6) * 12
    if firstpay == 300:
        payperyear = (1.044 - 0.6) * 12
    return round(payperyear, 1)


def calAB(years, firstpay, lifecost):
    '''

    :param years: 投资年数 2019年8月开始算起
    :param firstpay: 首付 200/250/300/400/500
    :param lifecost: 每年额外生活费用
    :return:
    '''
    years = years  # 投资年数 2019年8月开始算起
    amt1 = 30  # 目前流动资金
    amt2 = 260  # 半年后到期资金
    amt3 = 450  # 买金碧房子收入
    fundA = []  # 方式A每年资金池
    fundB = []  # 方式B每年资金池
    yearlist = []  # 记录年份
    rate1 = 0.105  # 年收益率
    rate2 = 0.04  # 半年收益率
    firstpay = firstpay  # 首付
    amt4 = loadpayperyear(firstpay)  # 每年供楼花费金额
    lifecost = lifecost  # 每年额外生活费用

    '''方式A'''
    # 这半年的投资本金 = 卖掉金碧的收入 + 目前流动资金 - 首付
    investamtA = amt3 + amt1 - firstpay

    # 半年后资金 = 这半年的投资本金 * (1+半年利率)
    wealthA = calincome1(investamtA, rate2)
    # print(wealth1)

    # 半年后总本金 = 半年后资金 + 半年后到期资金
    A2017 = wealthA + amt2

    # 第一个元素是2017年8月份左右的资金池
    fundA.append(A2017)

    # 2018年开始才需要预留资金还贷
    # 2018年资金池金额:
    temp2018 = calincome1(A2017, rate1)
    A2018 = temp2018 - amt4  # 扣去还贷额
    fundA.append(A2018)

    # 2019年计算资金池总额方法开始通用:
    # temp2019A = calincome1(A2018, rate1)  # 一部分是A2018的收益
    # temp2019B = calincome2(amt4, rate2)  # 一部分是还贷金额半年利息收益
    # A2019 = temp2019A + temp2019B - amt4 -lifecost # 2019年资金池总额 = A + B - 还贷金额 - 每年额外生活费用
    # fundA2019 = fundA_cal(A2018, rate1, amt4, rate2)
    # print(fundA2019)

    fundA_cal_years(A2018, rate1, amt4, rate2, years, fundA, lifecost)
    # print('方式A资金池:' + str(fundA))

    '''方式B'''
    # 这半年的投资本金 = 目前流动资金
    investamtB = amt1

    # 半年后资金 = 这半年的投资本金 * (1+半年利率)
    wealthB = calincome1(investamtB, rate2)
    # print(wealthB)

    # 半年后总本金 = 半年后资金 + 半年后到期资金
    B2017 = wealthB + amt2

    # 第一个元素是2017年8月份左右的资金池
    fundB.append(B2017)
    # print(fundB)

    fundB_cal(B2017, years + 1, years - 1, rate1, fundB, lifecost)
    # print('方式B资金池:' + str(fundB))

    for year in range(years + 2):
        yearlist.append(year + 2017)
    # print(yearlist)

    return (fundA, fundB, yearlist)


def calAB2(years, firstpay, lifecost):
    '''

    :param years: 投资年数 2019年8月开始算起
    :param firstpay: 首付 200/250/300/400/500
    :param lifecost: 每年额外生活费用
    :return:
    '''
    years = years  # 投资年数 2019年8月开始算起
    amt1 = 30  # 目前流动资金
    amt2 = 0  # 半年后到期资金
    amt3 = 500  # 买金碧房子收入
    rate1 = 0.08  # 年收益率
    rate2 = 0.04  # 半年收益率
    firstpay = firstpay  # 首付
    amt4 = loadpayperyear2(firstpay)  # 每年供楼花费金额
    lifecost = lifecost  # 每年额外生活费用

    fundA = []  # 方式A每年资金池
    fundB = []  # 方式B每年资金池
    yearlist = []  # 记录年份

    '''方式A'''
    # 这半年的投资本金 = 卖掉金碧的收入 + 目前流动资金 - 首付
    investamtA = amt3 + amt1 - firstpay

    # 半年后资金 = 这半年的投资本金 * (1+半年利率)
    wealthA = calincome1(investamtA, rate2)
    # print(wealth1)

    # 半年后总本金 = 半年后资金 + 半年后到期资金
    A2017 = wealthA + amt2

    # 第一个元素是2017年8月份左右的资金池
    fundA.append(A2017)

    # 2018年开始才需要预留资金还贷
    # 2018年资金池金额:
    temp2018 = calincome1(A2017, rate1)
    A2018 = temp2018 - amt4  # 扣去还贷额
    fundA.append(A2018)

    # 2019年计算资金池总额方法开始通用:
    # temp2019A = calincome1(A2018, rate1)  # 一部分是A2018的收益
    # temp2019B = calincome2(amt4, rate2)  # 一部分是还贷金额半年利息收益
    # A2019 = temp2019A + temp2019B - amt4 -lifecost # 2019年资金池总额 = A + B - 还贷金额 - 每年额外生活费用
    # fundA2019 = fundA_cal(A2018, rate1, amt4, rate2)
    # print(fundA2019)

    fundA_cal_years(A2018, rate1, amt4, rate2, years, fundA, lifecost)
    # print('方式A资金池:' + str(fundA))

    '''方式B'''
    # 这半年的投资本金 = 目前流动资金
    investamtB = amt1

    # 半年后资金 = 这半年的投资本金 * (1+半年利率)
    wealthB = calincome1(investamtB, rate2)
    # print(wealthB)

    # 半年后总本金 = 半年后资金 + 半年后到期资金
    B2017 = wealthB + amt2

    # 第一个元素是2017年8月份左右的资金池
    fundB.append(B2017)
    # print(fundB)

    fundB_cal(B2017, years + 1, years - 1, rate1, fundB, lifecost)
    # print('方式B资金池:' + str(fundB))

    for year in range(years + 2):
        yearlist.append(year + 2017)
    # print(yearlist)

    return (fundA, fundB, yearlist)
