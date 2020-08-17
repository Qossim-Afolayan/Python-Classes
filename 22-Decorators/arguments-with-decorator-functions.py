def be_nice(fnc):

    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you")
        print(args)
        fnc(*args, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")

    return inner
@be_nice
def complex_business_logic(stakeholder, position):
    print(f"Something  for our {position} {stakeholder}")


complex_business_logic("Boris", position = "CEO")


