from .stack import Stack

def par_check(par_string):
    s = Stack()

    for str in par_string:
        if str == '(':
            s.push(str)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()

print(f'result: {par_check('((((())))')}')