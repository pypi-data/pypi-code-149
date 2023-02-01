import shellt

def main():
    """Entry point for the application script"""
    print("Call your main application code here")

def run_test(script_file, function_name, args=[], mocks=[]):
    shellt.run_test(script_file, function_name, args, mocks)
