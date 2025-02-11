# Python StringBuilder

A project to emulate C#/Java StringBuilder using python's built-in list[str] class.

## Tools Used

| Tool    |  Version |
|:--------|---------:|
| Python  |   3.13.2 |
| VSCode  |   1.97.1 |
| PyCharm | 2024.3.2 |

## Change History

| Date       | Description                                                |
|:-----------|:-----------------------------------------------------------|
| 2025-02-06 | Initial creation                                           |
| 2025-02-07 | Simplify implementation using `list[str]` to hold contents |
| 2025-02-10 | Add more API documentation to README                       |
| 2025-02-11 | Add new methods to StringBuilder class                     |

## API Notes

### constructor: StringBuilder(value: str) or StringBuilder()
Accepts an optional initial `value`; otherwise, initializes to empty.

Example 1:

<code>
    sbr = StringBuilder()
</code>

Example 2:

<code>
    sbr = StringBuilder('ABCD')
</code>
    

### append(value: str)
Appends the specified string `value` to the string buffer.

Example:
<code>
    sbr = StringBuilder('ABCD')
    sbr.append("EFGH")
</code>
sbr now contains "ABCDEFGH"

### capacity()
See ```size()```


### delete(start_index: int, end_index: int)
Deletes characters from the string buffer beginning at ```start_index``` through and including ```end_index```

Example:

<code>
    sbr = StringBuilder('ABCDE' * 4)
    start_index = 0
    end_index = 3
    sbr.delete(start_index, end_index)
</code>
After delete(0, 3), the buffer contains "EABCDEABCDEABCDE"

### index_of(value:str)
Returns either the index of the start of `value` or -1 if `value` does not exist in the buffer.

Example:
<code>
    sbr = StringBuilder('ABCD')
    idx = sbr.index_of("C") # returns 2    
</code>
idx will contain a value of 2.

### insert(index: int, value: str)
Inserts the specified string `value` at the specified `index`,
pushing the remainder of the entry to the right by
the length of the `value`.

Example:
<code>
    sbr = StringBuilder("A B C X Y Z ")
    index = sbr.index_of('X ')
    value_to_insert = 'J K L '
    sbr.insert(index, value_to_insert)
</code>

after adding "J K L " at index = 6: sbr = "A B C J K L X Y Z "


### last_index_of(search_for:str)
Returns the index of the last occurrence of the specified string search value or -1 if not found.

<code>
    sbr = StringBuilder('ABCDE' * 4)
    search_for = 'CD'
    idx = sbr.last_index_of(search_for)
</code>
The last occurrence of "CD" within "ABCDEABCDEABCDEABCDE" is at position 17

### remove(index: int, length: int)
Removes `length` characters from the buffer starting at `index`. 

Example:
<code>
    sbr = StringBuilder("A B C J K L X Y Z ")
    remove = 'X Y Z '
    length = len(remove)
    index = sbr.index_of(remove)
    sbr.remove(index, length)
</code>
after removing "X Y Z " starting at 12 for a length of 6: sbr = "A B C J K L "

### replace(old_value:str, new_value:str)
Replaces all occurrences of `old_value` with `new_value`.

Example:
<code>
    sbr = StringBuilder('abcd' * 3)
    find = 'b'
    replace = 'B'
    sbr.replace(find,replace)
</code>
After replacing "b" with "B", sbr = "aBcdaBcdaBcd"

### reverse()
Reverses the string inside the underlying buffer

Example:
<code>
    sbr = StringBuilder('ABCDE')
    print(f'Before revers(), sbr = "{sbr}"')
    sbr.reverse()
    print(f'After reverse(), sbr = "{sbr}"')
</code>
Before reverse(), sbr = "ABCDE"
<br/>
After reverse(), sbr = "EDCBA"

### size()
Returns the current size of the buffer as an integer.

Example:
<code>
    sbr = StringBuilder('abcd' * 3)
    lth = sbr.size()
</code>
lth will contain the integer value 12.

### to_string()
Returns the StringBuffer contents as a python string (str).

Example:
<code>
    sbr = StringBuilder('abcd' * 3)
    x = sbr.to_string())
</code>
x will contain "abcdabcdabcd"

## References
* [Using the StringBuilder class in .Net](https://learn.microsoft.com/en-us/dotnet/standard/base-types/stringbuilder)
* [C# StringBuilder class API](https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=net-9.0)
* [Java StringBuilder class API](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html)
