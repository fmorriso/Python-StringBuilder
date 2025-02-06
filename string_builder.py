from io import StringIO


class StringBuilder(StringIO):
    """ Implements a better StringIO API without the annoying constructor flaw of StringIO """


    def __init__(self, initial_value = ''):
        """ Initialize an instance of the class without the flaw of the underlying parent class, StringIO"""
        super().__init__(initial_value)
        # HERE IS WHERE WE OVERCOME THE DESIGN FLAW IN STRINGIO:
        super().seek(len(initial_value))


    def append(self, new_value: str) -> None:
        """ append the specified string to the end of the buffer."""
        super().write(new_value)


    def __str__(self) -> str:
        return super().getvalue()
