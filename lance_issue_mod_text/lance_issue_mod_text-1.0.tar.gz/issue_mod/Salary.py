'''
用于计算薪资的模块
'''

company = 'xx公司'
print(company)

def yearsalary(monthsalary):
    '''
    计算年薪，monthsalary*12
    :param monthsalary:传入月薪
    :return:返回年薪
    '''
    return monthsalary*12

def daysalary(monthsalary):
    '''
    计算日薪，22.5天法定工作日
    :param monthsalary:传入月薪
    :return: 返回日薪
    '''
    return monthsalary/22.5


# 测试代码
if __name__ == '__main__':
    print(yearsalary(10000))