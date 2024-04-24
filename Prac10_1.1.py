#Ujjwal Shelke
class NameInvalidException(Exception):
    pass


def get_name():
    name = input("Enter your name (10 alphabet characters only): ")
    if len(name) != 10:
        raise NameInvalidException
    return name


try:
    name = get_name()
    print("Hello, " + name + "!")
except NameInvalidException:
    print("Invalid name")