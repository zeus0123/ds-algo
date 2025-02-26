from .stack import Stack

def complex_parenthesis(par_string):
    s = Stack()

    for str in par_string:
        if str in '({[':
            s.push(str)
        else: 
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), str):
                    return False
                
    return s.is_empty()

def matches(left, right):
    all_left = '[{('
    all_right = ')}]'

    return all_left.index(left) == all_right.index(right)