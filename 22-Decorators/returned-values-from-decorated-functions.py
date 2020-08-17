def be_nice(fnc):

    def inner(*arg, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you")
        result = fnc(*arg, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")
        return result

    return inner
@be_nice
def complex_business_sum(a, b):
    return a + b

print(complex_business_sum(a = 3, b = 5))
