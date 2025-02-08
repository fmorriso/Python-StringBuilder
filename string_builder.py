class StringBuilder:
    """A roughly equivalent C# StringBuilder written with Python 3"""


    def __init__(self, initial_value = ''):
        """ Initialize an instance of the class from the initial value."""
        self._chars: list[str] = list(initial_value)


    def append(self, new_value: str) -> None:
        """ append the specified string to the end of the existing string."""
        self._chars.extend(list(new_value))


    def insert(self, index: int, new_value: str) -> None:
        """ insert the specified string at the specified index_of within the buffer."""
        self._chars[index:index] = list(new_value)  # new_list


    def index_of(self, search_for: str) -> int:
        """ Return the index of the specified string within the buffer."""
        if search_for is None or len(search_for) == 0:
            return -1

        # special case of single character to search for
        if len(search_for) == 1:
            if search_for in self._chars:
                return self._chars.index(search_for)

        # The string to search for is multiple characters, so need different approach.
        full_string = ''.join(self._chars)
        if search_for in full_string:
            return full_string.index(search_for)
        return -1


    def size(self) -> int:
        return len(self._chars)


    def remove(self, start_index: int, length: int) -> None:
        """ Remove the specified portion of the string starting at start_index for
        the number of characters specified by length."""
        del self._chars[start_index:start_index + length]


    def replace(self, old_value: str, new_value: str) -> None:
        """ Replace all occurrences of the specified string with the specified value."""
        if len(old_value) == 0:
            return
        # single character replacement can be done quickly
        if len(new_value) == 1:
            self._chars = [new_value if item == old_value else item for item in self._chars]
        else:
            # multiple character replacement needs special treatment as a string
            full_string = ''.join(self._chars)
            new_string = full_string.replace(old_value, new_value)
            self._chars = list(new_string)

    def to_string(self) -> str:
        return ''.join(self._chars)

    def __str__(self) -> str:
        # print(f'{self._chars = }')
        return ''.join(self._chars)
