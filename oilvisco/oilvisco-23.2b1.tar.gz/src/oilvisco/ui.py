"""
User Inetrface.
"""
from oilvisco.datatypes import Oil

def getinput(typ_prompt="Which oil? : ", amount_prompt="How many (in l)? : "):
    """
    takes two strings presenting the user inputs for oiltype and amount
    returns a strin in the format: oiltype x amount, e.g: '0w10x3'
    """
    oiltype = input(typ_prompt)
    if not "w" in oiltype.lower():
        return None
    if "x" in oiltype.lower():
        oiltype, oilunits = oiltype.lower().split('x', 1)
    else:
        oilunits = input(amount_prompt)
    if not oilunits.isdecimal():
        return None

    return f'{oiltype}x{oilunits}'


def convert_input(inputstr):
    """
    takes str like "0w20x3 10w40x1" and 
    returns a list like [(0,20,3), (10, 40,1)]
    """
    oilstr=inputstr.lower().split()
    values = []
    for substr in oilstr:
        typ, units = substr.split('x')
        lower, upper = typ.split('w')
        values.append(Oil(int(lower), int(upper), int(units)))

    return values


def inputloop():
    inputs = []
    while True:
        userinput = getinput()
        # check if invalid input is meant as loop abortion
        if not userinput and input("Done? (y/n): ").startswith("y"):
            break
        elif not userinput:
            continue
            
        try:
            converted = convert_input(userinput)
            inputs.append(*converted)
        except:
            print("Last input was invalid! Input must be 'number W number, e.g.: 0w10'. Retry!") 
    return inputs

