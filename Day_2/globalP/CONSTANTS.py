_PI = 22/7
_NO_Of_Days=7
_NO_Of_Months=12

__all__ = ['addition', '_multiArguments']

def addition():
    pass

def subtraction():
    pass

def _multiArguments(*params):
    temp = []
    for i in params:
        temp.append(i)
    return " ".join(temp)

def _multiArguments2(**params):
    temp = {}
    for i, k in params.items():
        temp[i] = k
    return temp