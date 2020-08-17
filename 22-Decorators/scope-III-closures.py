def outer():
    candy = "Snickers"
    def inner():
        return candy

    return inner()
the_func = outer()
print(the_func)

def multiply(a, b):

  return a * b



def divide(a, b):

  return a / b



def calculate(func, a, b):

  return func(a, b)



print(calculate(multiply, 10, 5))
def a():

  def b():
    val = 50

    def c():
        return val

    return c()

  return b()



print(a())

val = "Hello"