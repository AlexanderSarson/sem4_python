import string


class InvalidArgumentException(Exception):
    def __init__(self, message):
        error_message = f"Error message : {message}."
        super().__init__(error_message)


class Person():
    def __init__(self, name):
        self.name = name

    def checkName(self):
        try:
            for word in self.name.split(" "):
                if word[0] != word[0].upper():
                    raise InvalidArgumentException(
                        "Name does not start with capital letter")
                for letter in word:
                    if string.ascii_letters.find(letter) == -1:
                        raise InvalidArgumentException("Invalid char in name")
        except InvalidArgumentException as ex:
            print(ex)
        else:
            print("Name is valid")


name = Person("Alexander Sarson")

name.checkName()
