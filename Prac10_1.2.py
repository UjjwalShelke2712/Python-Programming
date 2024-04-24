#84158 Ujjwal Shelke
class InvalidUserException(Exception):
    pass


def get_validate():
    str = input("Enter your 4 digit password: ")
    oldpass = "1234"
    if oldpass != str:
        raise InvalidUserException
    return str


try:
    str = get_validate()
    print(f"Hello! Your Validation is Done")
except InvalidUserException:
    print("Validation failed.....!")