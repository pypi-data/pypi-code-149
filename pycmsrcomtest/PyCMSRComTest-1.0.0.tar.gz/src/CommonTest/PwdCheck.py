#coding=utf-8
__author__ = 'yujingrong'

import importlib, sys
importlib.reload(sys)

keys = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']','\\'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '','\''],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']]

keys2 = [['1', 'q', 'a', 'z'],
        ['2', 'w', 's', 'x'],
        ['3', 'e', 'd', 'c'],
        ['4', 'r', 'f', 'v'],
        ['5', 't', 'g', 'b'],
        ['6', 'y', 'h', 'n'],
        ['7', 'u', 'j', 'm'],
        ['8', 'i', 'k', ','],
        ['9', 'o', 'l', '.'],
        ['0', 'p', '', '/'],
        ['-', '[', '\'']]

keys3 = [['a', 'w', '3'],
        ['z', 's', 'e', '4'],
        ['x', 'd', 'r', '5'],
        ['c', 'f', 't', '6'],
        ['v', 'g', 'y', '7'],
        ['b', 'h', 'u', '8'],
        ['n', 'j', 'i', '9'],
        ['m', 'k', 'o', '0'],
        [',', 'l', 'p', '-'],
        ['.', '', '[', '='],
        ['/', '\'', ']']]

keys4 = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],]

# 键盘连续性
def isKeyboardContinuous(pwd):
    try:
        return keyS(keyVariation(pwd, keys), keyVariation(pwd, keys2), keyVariation(pwd, keys3), keyVariation(pwd, keys4))
    except:
        return False

def keyS(b1, b2, b3, b4):
    if (1-b1) and (1-b2) and (1-b3) and (1-b4):
        return False
    return True

def keyVariation(pwd, keys):
    isTrue = False
    pwdChars = getChars(pwd)
    list = []
    for k in range(len(pwdChars)):
        for i in range(len(keys)):
            for j in range(len(keys[i])):
                if keys[i][j] == pwdChars[k]:
                    list.append(str(i) + "," + str(j))
    if list == []:
        return False
    index = 1
    tmpY = int(list[0].split(',')[0])
    tmpX = int(list[0].split(',')[1])
    for i in range(1, len(list)):
        y = int(list[i].split(",")[0])
        x = int(list[i].split(",")[1])
        if tmpY == y:
            if tmpX - x == -1:
                tmpX = x
                index += 1
                if index > 2:
                    break
                continue
            else:
                tmpY = y
                tmpX = x
                index = 1
                continue
        else:
            index = 1
            tmpX = x
            tmpY = y
    if index < 3:
        tmpY = int(list[0].split(",")[0])
        tmpX = int(list[0].split(",")[1])
        for i in range(1, len(list)):
            y = int(list[i].split(",")[0])
            x = int(list[i].split(",")[1])
            if tmpY == y:
                if tmpX - x == 1:
                    tmpX = x
                    index += 1
                    if index > 2:
                        break
                    continue
                else:
                    tmpY = y
                    tmpX = x
                    index = 1
                    continue
            else:
                index = 1
                tmpX = x
                tmpY = y
    if index > 2:
        isTrue = True
    return isTrue


# 特殊字符转换
def getChars(pwd):
    pwdChars = pwd.lower()
    if "!" in pwdChars:
        pwdChars = pwdChars.replace("!", "1")
    if "@" in pwdChars:
        pwdChars = pwdChars.replace("@", "2")
    if "#" in pwdChars:
        pwdChars = pwdChars.replace("#", "3")
    if "$" in pwdChars:
        pwdChars = pwdChars.replace("$", "4")
    if "￥" in pwdChars:
        pwdChars = pwdChars.replace("￥", "4")
    if "%" in pwdChars:
        pwdChars = pwdChars.replace("%", "5")
    if "^" in pwdChars:
        pwdChars = pwdChars.replace("^", "6")
    if "&" in pwdChars:
        pwdChars = pwdChars.replace("&", "7")
    if "*" in pwdChars:
        pwdChars = pwdChars.replace("*", "8")
    if "(" in pwdChars:
        pwdChars = pwdChars.replace("(", "9")
    if ")" in pwdChars:
        pwdChars = pwdChars.replace("*", "0")
    if "_" in pwdChars:
        pwdChars = pwdChars.replace("_", "-")
    if "+" in pwdChars:
        pwdChars = pwdChars.replace("+", "=")
    if "{" in pwdChars:
        pwdChars = pwdChars.replace("{", "[")
    if "}" in pwdChars:
        pwdChars = pwdChars.replace("}", "]")
    if "|" in pwdChars:
        pwdChars = pwdChars.replace("|", "\\")
    if ":" in pwdChars:
        pwdChars = pwdChars.replace(":", "")
    if "\"" in pwdChars:
        pwdChars = pwdChars.replace("\"", "\'")
    if "<" in pwdChars:
        pwdChars = pwdChars.replace("<", ",")
    if ">" in pwdChars:
        pwdChars = pwdChars.replace(">", ".")
    if "?" in pwdChars:
        pwdChars = pwdChars.replace("?", "/")
    return pwdChars

# 用户无关性校验
def isUserContact(pwd, name):
    try:
        if name is None:
            return False
        newName = toChangeCharSimilar(name)
        newPwd = toChangeCharSimilar(pwd)
        if newName in newPwd:
            return True
        if len(newName) > 5:
            for i in range(len(newName) - 4):
                substring = newName[i:(i+5)]
                if substring in newPwd:
                    return True
            return False
        return False
    except:
        return False

# 判断连续三次重复字符
def threeTimesChar(pwd):
    try:
        chars = getChars(pwd)
        for i in range(len(chars)-2):
            if chars[i] == chars[i+1]:
                if chars[i] == chars[i+2]:
                    return True
        return False
    except:
        return False

# 形相似字符串转换
def toChangeCharSimilar(name):
    pwdLower = name.lower()
    if "!" in pwdLower:
        pwdLower = pwdLower.replace("!", "1")
    if "o" in pwdLower:
        pwdLower = pwdLower.replace("o", "0")
    if "i" in pwdLower:
        pwdLower = pwdLower.replace("i", "1")
    if "z" in pwdLower:
        pwdLower = pwdLower.replace("z", "2")
    if "i" in pwdLower:
        pwdLower = pwdLower.replace("i", "1")
    if "@" in pwdLower:
        pwdLower = pwdLower.replace("@", "a")
    if "$" in pwdLower:
        pwdLower = pwdLower.replace("$", "s")
    if "l" in pwdLower:
        pwdLower = pwdLower.replace("l", "1")
    if "|" in pwdLower:
        pwdLower = pwdLower.replace("|", "1")
    if "&" in pwdLower:
        pwdLower = pwdLower.replace("&", "8")
    if "s" in pwdLower:
        pwdLower = pwdLower.replace("s", "5")
    if "@" in pwdLower:
        pwdLower = pwdLower.replace("@", "a")
    if "q" in pwdLower:
        pwdLower = pwdLower.replace("q", "9")
    return pwdLower

# 全角字符串转半角字符串
def ToDBc(input):
    rstring = ""
    for uchar in input:
        inside_code = ord(uchar)
        if inside_code == 12288:                            # 全角空格直接转换
            inside_code = 32
        elif 65281 <= inside_code <= 65374:   				# 全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring

# 判断字符串中是否含有中文或者中文字符
def isChinese(str):
    for ch in str.encode("utf-8").decode("utf-8"):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

# 判断是否包含空格
def isIncludeEmpty(str):
    try:
        if " " in str:
            return True
    except:
        return False

# 特殊字符、数字、字母 3选3
def isLetterDigit(s):
    if (len(s) > 16) or (len(s) < 8):
        return False
    isDigit = False
    isLetter = False
    isSpecial = False
    symbol= ['.','`','~', '!','$', '@', '#', '%', '^', '&', '*','{', '}',
             '(', ')', '+','-', '=', '"', ',', '.', '?', '[', ']',
             '\\','\'',':',';','|','/','<','>','?','_','.']
    for i in range(len(s)):
        if s[i].isalpha:
            isLetter = True
        if s[i].isdigit:
            isDigit = True
        if s[i] in symbol:
            isSpecial = True
    isRight = isDigit and isLetter and isSpecial
    return isRight

#  弱口令校验的主方法，返回True表示是弱密码
def checkPw(password, name):
    if password is None:
        return False
    flag = False
    b = int(isChinese(password))
    password = ToDBc(password)
    b1 = int(isKeyboardContinuous(password))
    b2 = int(threeTimesChar(password))
    b3 = int(isUserContact(password, name))
    result = b + b1 + b2 + b3
    if result > 0:
        flag = True
    return flag

if __name__ == '__main__':
    # print(getChars("!@#$"))
    # print(keyVariation("!@#", keys))
    # print(keyVariation("!@#", keys2))
    # print(keyVariation("!@#", keys3))
    # print(keyVariation("!@#$", keys4))
    # print(isKeyboardContinuous("@Aa1234567"))
    # print(threeTimesChar("@Jy710817222"))
    # print(toChangeCharSimilar("@!abc"))
    # print(isChinese("余uuuu"))
    # print(isLetterDigit("Ac#123123"))
    print(checkPw("@Jy7108172", 'yujingrong'))