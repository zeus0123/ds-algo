from .stack import Stack

def divide_by_2(decimal_num):
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % 2
        print(rem)
        rem_stack.push(rem)
        decimal_num = decimal_num // 2

    bin_str = ''
    while not rem_stack.is_empty():
        bin_str = bin_str + str(rem_stack.pop())

    return bin_str

print(divide_by_2(8))