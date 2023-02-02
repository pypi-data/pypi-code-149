#该自定义函数实现计算一个自然数需要多少根火柴棒
def match_num(num):
    f=[6,2,5,5,4,5,6,3,7,6]    #数字0~9各需要的火柴棒数
    total=0
    if num==0:
        total=f[0]
    else:
        while (num>0):
            x=num%10           #取num除以10的余数，即num的个位数
            total=total+f[x]   #所需火柴棒相加
            num=num//10        #num整除10，去掉num的个位数，得到剩余数位上的数字
    return total               #返回需要多少根火柴棒数
            
