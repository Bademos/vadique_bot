a = 1
b = 2
c = "shitbowl"

def func_1():
    print(a)

def func_2():
    print(c)

def tsr():
    print(__name__)

__all__ = [a, func_2, tsr]
