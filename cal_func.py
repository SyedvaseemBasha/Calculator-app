def do_addition(a:int,b:int):
    return a + b

def do_Subtraction(a:int,b:int):
    return a - b

def do_Division(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return 'Cannot divided by zero'