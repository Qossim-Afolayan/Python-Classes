def be_nice(fnc):

    def inner():
        print("Nice to meet you! I'm honored to execute your function for you")
        fnc()
        print("It was my pleasure executing your function! Have a nice day!")

    return inner
@be_nice
def complex_business_logic():
    print("Something complex")

# be_nice(complex_business_logic)()
complex_business_logic()

@be_nice
def another_fancy_function():
    print("AlhamduliLLah")

another_fancy_function()

