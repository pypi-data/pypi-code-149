import base64


def add_one(number):
    return number + 1


# 小写26个字母
SC26 = []
for one in range(97, 123):
    # c26.append(chr(one).capitalize())
    SC26.append(chr(one))

# 大写26个字母
BC26 = []
for i in range(65, 91):
    BC26.append(chr(i))

B26 = ''.join(BC26)  # 'A-Z'
S26 = ''.join(SC26)  # 'a-z'
B62 = ''.join(BC26[::-1])  # 'Z-A' 倒序
S62 = ''.join(SC26[::-1])  # 'z-a' 倒序
a09 = '0123456789'
a90 = '9876543210'


# 加密
def enc(s):
    if str(s) == 'null':
        print('null', s)
        return '***此处有空值***'
    elif s is None:
        print('None', s)
        return '***此处有None值***'
    else:
        return str(base64.b64encode(s.encode("utf-8")), "utf-8")


# 自定义加密
def ens(s):
    if str(s) == 'null':
        print('null', s)
        return '***此处有空值***'
    elif s is None:
        print('None', s)
        return '***此处有None值***'
    else:
        bstr = str(base64.b64encode(s.encode("utf-8")), "utf-8")
        ers = []
        for x in range(0, len(bstr)):
            if (bstr[x]).isdigit():
                ers.append(a90[int(bstr[x])])
            elif B26.find(bstr[x]) > -1:
                ers.append(B62[int(B26.find(bstr[x]))])
            elif S26.find(bstr[x]) > -1:
                ers.append(S62[int(S26.find(bstr[x]))])
            else:
                ers.append(bstr[x])

        return ''.join(ers)


# 解密
def dec(oao):
    return str(base64.b64decode(oao), "utf-8")


# 自定义解密
def des(oao):
    drs = []
    for a in range(0, len(oao)):
        if (oao[a]).isdigit():
            drs.append(a90[int(oao[a])])
        elif B62.find(oao[a]) > -1:
            drs.append(B26[int(B62.find(oao[a]))])
        elif S62.find(oao[a]) > -1:
            drs.append(S26[int(S62.find(oao[a]))])
        else:
            drs.append(oao[a])

    rer = ''.join(drs)
    return str(base64.b64decode(rer), "utf-8")
