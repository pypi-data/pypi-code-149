# Create 9 stacks such that each stack is a dictionary item with string keys 1-9 and a list for a value
stacks = dict()
for i in range(1,10):
    stacks[str(i)] = []

stacks['1'] = ['D','T','R','B','J','L','W','G']
stacks['2'] = ['S','W','C']
stacks['3'] = ['R','Z','T','M']
stacks['4'] = ['D','T','C','H','S','P','V']
stacks['5'] = ['G','P','T','L','D','Z']
stacks['6'] = ['F','B','R','Z','J','Q','C','D']
stacks['7'] = ['S','B','D','J','M','F','T','R']
stacks['8'] = ['L','H','R','B','T','V','M']
stacks['9'] = ['Q','P','D','S','V']


#create a function that moves items from one stack to another
#the function should have the following parameters: source_stack_number, destination_stack_number, number_of_items
def move(number_of_items,source_stack_number, destination_stack_number):
    global stacks
    for i in range(number_of_items):
        stacks[destination_stack_number].append(stacks[source_stack_number].pop())


instructions = open('input.txt', 'r').readlines()
for instruction in instructions:
    instruction = instruction.split()
    print(instruction)
    move(int(instruction[1]), instruction[3], instruction[5])
    for stack in stacks:
        print(stack, stacks[stack])
    print('-------------------------')
