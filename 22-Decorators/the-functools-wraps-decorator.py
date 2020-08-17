import functools

def be_nice(fnc):
    @functools.wraps(fnc)
    def inner(*arg, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you")
        result = fnc(*arg, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")
        return result

    return inner
@be_nice
def complex_business_sum(a, b):
    "Adds two numbers together"
    return a + b

print(complex_business_sum(a = 3, b = 5))

# help(complex_business_sum)

import functools



def uppercase(fn):

    @functools.wraps(fn)

    def wrapper(*args, **kwargs):

        fn(*args, **kwargs).upper()
        



    return wrapper



@uppercase

def concatenate(a, b):

    """Combines two strings together"""

    return a + b

print(concatenate("pyt", "hon"))