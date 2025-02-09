# Python StringBuilder

A project to emulate C#/Java StringBuilder using python's built-in list[str] class.

## Tools Used

| Tool    |  Version |
|:--------|---------:|
| Python  |   3.13.2 |
| VSCode  |   1.96.4 |
| PyCharm | 2024.3.2 |

## Change History

| Date       | Description                                                |
|:-----------|:-----------------------------------------------------------|
| 2025-02-06 | Initial creation                                           |
| 2025-02-07 | Simplify implementation using `list[str]` to hold contents |

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
</code>
<div></div>
<code>    
    sbr.append("EFGH")
</code>

### index_of(value:str)
Returns either the index of the start of `value` or -1 if `value` does not exist in the buffer.


Example:

<code>
    sbr = StringBuilder('ABCD')
</code>
<div></div>
<code> 
    idx = sbr.index_of("C") # returns 2    
</code>

### insert(index: int, value: str)
Inserts the specified string `value` at the specified `index`,
pushing the remainder of the entry to the right by
the length of the `value`.

### remove(index: int, length: int)
Removes `length` characters from the buffer starting at `index`. 


### replace(old_value:str, new_value:str)
Replaces all occurrences of `old_value` with `new_value`.

### size()
Returns the current size of the buffer as an integer.

### to_string()
Returns the StringBuffer contents as a python string (str).

## References
* [Using the StringBuilder class in .Net](https://learn.microsoft.com/en-us/dotnet/standard/base-types/stringbuilder)
* [StringBuilder class API](https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=net-9.0)