import sys
from string_builder import StringBuilder


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def main():
    sbr = StringBuilder('A B C ')
    print(f'Initial sbr="{sbr}"')
    sbr.append('X ')
    sbr.append('Y ')
    sbr.append('Z ')
    print(f'After appends, sbr="{sbr}"')

    # try inserting a new string at a specific point in the existing string
    index = sbr.index_of('X ')
    value_to_insert = 'J K L '
    sbr.insert(index, value_to_insert)
    print(f'after inserting "{value_to_insert}" at {index = }: sbr = "{sbr}"')

    # try removing 'X Y Z'
    remove = 'X Y Z '
    length = len(remove)
    index = sbr.index_of(remove)
    if index >= 0:
        sbr.remove(index, length)
        print(f'after removing "{remove}" starting at {index} for a length of {length}: sbr = "{sbr}"')
    else:
        print(f'"{remove}" was not found in the string builder instance')

    # practice replace method with single character replacement
    sbr = StringBuilder('abcd' * 3)
    print(f'sbr = "{sbr}"')
    find = 'b'
    replace = 'B'
    sbr.replace(find, replace)
    print(f'After replacing "{find}" with "{replace}", sbr = "{sbr}"')

    # practice replace method with multi-character replacement
    find = 'cd'
    replace = 'CD'
    sbr.replace(find, replace)
    print(f'After replacing "{find}" with "{replace}", sbr = "{sbr}"')

    print(f'{sbr = }')

    lth = sbr.size()
    print(f'{lth = }')

    print(sbr)  # calls __str__
    print(f'{sbr}')  # calls __repr__

    # test last_index_of
    sbr = StringBuilder('ABCDE' * 4)
    search_for = 'E'
    idx = sbr.last_index_of(search_for)
    print(f'The last occurrence of "{search_for}" within "{sbr.to_string()}" is at position {idx}')
    search_for = 'CD'
    idx = sbr.last_index_of(search_for)
    print(f'The last occurrence of "{search_for}" within "{sbr.to_string()}" is at position {idx}')

    # test delete
    sbr = StringBuilder('ABCDE' * 4)
    start_index = 0
    end_index = 3
    sbr.delete(start_index, end_index)
    print(f'After delete({start_index}, {end_index}), the buffer contains "{sbr.to_string()}"')

    # test reverse
    sbr = StringBuilder('ABCDE')
    print(f'Before reverse(), sbr = "{sbr}"')
    sbr.reverse()
    print(f'After reverse(), sbr = "{sbr}"')

    # test replace(start, end, value)
    sbr = StringBuilder('ABCDEFG')
    print(f'Original sbr = "{sbr}"')
    replacement = "WXYZ"
    start_index = sbr.index_of("C")
    end_index = start_index + 1
    sbr.replace_at(start_index, end_index, replacement)
    print(f'After replace_at({start_index}, {end_index}, "{replacement}"), sbr = "{sbr}"')


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()
