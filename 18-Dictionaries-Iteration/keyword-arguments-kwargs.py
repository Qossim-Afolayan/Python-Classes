def collect_keyword_parameters(**kwargs):
    print(kwargs)
    print(type(kwargs))

collect_keyword_parameters(a = 2, b = 3, c = 4)

def args_and_kwargs(a, b, *args, **kwargs):
    print(f"The sum of a and b is {a + b}")
    print(f"The sum of the args is {sum(args)}")

    dict_sum = 0

    for key, value in kwargs.items():
        dict_sum += value
    print(f"The sum of the kwargs dictionary is {dict_sum}")

args_and_kwargs(1, 2, 3, 4, 5, 6, x = 7, y = 8, z = 10)

