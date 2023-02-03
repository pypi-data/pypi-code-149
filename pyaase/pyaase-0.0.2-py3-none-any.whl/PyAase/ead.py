import base64

# lower letters 26
L26 = []
#  upper letters 26
U26 = []
n09 = '0123456789'
n90 = '9876543210'
for i in range(97, 123):
    # capitalize() capitalize the first letter
    # upper() All letters uppercase
    U26.append(chr(i).upper())
    L26.append(chr(i))

B26 = ''.join(U26)  # 'A-Z'
S26 = ''.join(L26)  # 'a-z'
B62 = ''.join(U26[::-1])  # 'Z-A' inverted order
S62 = ''.join(L26[::-1])  # 'z-a' inverted order


# encryption by base64
def enc_base64(temp_str):
    return str(base64.b64encode(temp_str.encode("utf-8")), "utf-8")


# decryption by base64
def dec_base64(temp_str):
    return str(base64.b64decode(temp_str), "utf-8")


# change letter order
def clo(temp_str, _type='enc'):
    sublist = []
    if _type == 'enc':
        sub_digit = n90
        sub_big = B26
        sub_gib = B62
        sub_small = S26
        sub_lams = S62
    else:
        sub_digit = n09
        sub_big = B62
        sub_gib = B26
        sub_small = S62
        sub_lams = S26

    if temp_str is None:
        return 'AED Error: ***The value here is None***The value is: %s' % temp_str
    else:
        substr = temp_str
        for x in range(len(substr)):
            if (substr[x]).isdigit():
                sublist.append(sub_digit[int(substr[x])])
            elif (substr[x]).isupper():
                sublist.append(sub_gib[int(sub_big.find(substr[x]))])
            elif (substr[x]).islower():
                sublist.append(sub_lams[int(sub_small.find(substr[x]))])
            else:
                sublist.append(substr[x])

        return ''.join(sublist)
