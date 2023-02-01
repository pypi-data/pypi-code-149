"""
calculate the blended oil viscosity of motor oils.
"""
from .ui import inputloop
from .calc import blend

def start():
    inputs = inputloop()
    blended_oil = blend(inputs)

    print(f'The resulting oil of {blended_oil.liter} liters has the type: {blended_oil.lower}W{blended_oil.upper}')

    


if __name__ == "__main__":
    start()
