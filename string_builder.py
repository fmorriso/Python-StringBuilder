from io import StringIO

class StringBuilder():

    def __init__(self, initial_value = ''):
        self.value = initial_value
        self.buffer = StringIO(initial_value)
        # HERE IS WHERE WE OVERCOME THE DESIGN FLAW IN STRINGIO:
        self.buffer.seek(len(initial_value))

    def append(self, new_value: str) -> None:
        self.buffer.write(new_value)

    def __str__(self) -> str:
        return self.buffer.getvalue()