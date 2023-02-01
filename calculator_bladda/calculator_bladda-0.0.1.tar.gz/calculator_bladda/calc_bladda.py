class CalcBladda(object):
    """Calculator package by Adda Blaise"""
    pass

    def __init__(self, memory_value: float = 0) -> None:
        """Initialize the constructor with a memory value of 0"""
        self.memory_value = memory_value
        
    def memory(self):
        """Returns the current value of memory_value"""
        return self.memory_value
    
    def add(self, input_number: float):
        """ Adds the input_value to the memory_value"""
        self.memory_value += input_number
        return self.memory_value
    
    def subtract(self, input_number: float):
        """ Subtracts the input_value from the memory_value"""
        self.memory_value -= input_number
        return self.memory_value
    
    def multiply(self, input_number: float):
        """ Multiplies the input_value with the memory_value"""
        self.memory_value *= input_number
        return self.memory_value
    
    def divide(self, input_number: float):
        """ Divides the input_value with the memory_value"""
        self.memory_value /= input_number
        return self.memory_value
    
    def nth_root(self, input_number: float):
        """ Returns the nthroot"""
        if self.memory_value <= 0:
            return 'Current value is negative'
        elif input_number <= 0:
            return 'Root value cannot be negative'
        else:
            self.memory_value = self.memory_value**(1/input_number)
            return self.memory_value
        
    
    def reset(self):
        """ Resets the memory_value to 0"""
        self.memory_value = 0
    
# Usage example 
"""
* Show memory value             calc.memory()
* Addition                      calc.add(number)
* Subtraction                   calc.subtract(number)
* Multiplication                calc.multiply(number)
* Division                      calc.divide(number)
* nth root of a number          calc.nth_root(n)
* Reset                         calc.reset()
    
>>>>calc = CalcBladda()
>>>>calc.add(10)
10
>>>>calc.subtract(2)
8
>>>>calc.multiply(3)
24
>>>>calc.divide(2)
12.0
>>>>calc.nth_root(2)
3.4641
"""