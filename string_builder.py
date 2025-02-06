from io import StringIO


class StringBuilder(StringIO):
    """ Implements a better StringIO API without the annoying constructor flaw of StringIO """


    def __init__(self, initial_value = ''):
        super().__init__(initial_value)
        # HERE IS WHERE WE OVERCOME THE DESIGN FLAW IN STRINGIO:
        super().seek(len(initial_value))


    def append(self, new_value: str) -> None:
        super().write(new_value)


    def __str__(self) -> str:
        return super().getvalue()
