#gloobal scope
def outer():
    #Enclosing function scope 

    def inner():
        #local scope
        return len

    return inner()

print(outer()("pytrhon"))