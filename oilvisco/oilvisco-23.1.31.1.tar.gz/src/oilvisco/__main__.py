"""
calculate the blended oil viscosity of motor oils.
"""
from .ui import inputloop, convert_input
from .calc import blend


from os import path
import sys



def batch(fname):
    with open(fname) as f:
        lines = f.read()
        blended_oil = blend(convert_input(lines))

    print(f'The resulting oil of {blended_oil.liter} liters has the type: {blended_oil.lower}W{blended_oil.upper}')


def start():
    """
    normal entrypoint.
    `mische` script entrypoint.
    """
    if sys.argv and len(sys.argv) > 1:
        fname = sys.argv[1] if path.isfile(sys.argv[1]) else None
        if fname:
            batch(fname)
            return

    inputs = inputloop()
    blended_oil = blend(inputs)

    print(f'The resulting oil of {blended_oil.liter} liters has the type: {blended_oil.lower}W{blended_oil.upper}')

    


if __name__ == "__main__":
    start()
