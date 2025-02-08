import sys
from string_builder import StringBuilder


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def main():
    sbr = StringBuilder('A B C ')
    sbr.append('X ')
    sbr.append('Y ')
    sbr.append('Z ')
    print(sbr)

    # try inserting a new string at a specific point in the existing string
    index = sbr.index_of('X ')
    sbr.insert(index, 'J K L ')
    print(f'after adding J K L: {sbr.to_string() = }')

    # try removing 'X Y Z'
    remove = 'X Y Z '
    length = len(remove)
    index = sbr.index_of(remove)
    if index >= 0:
        sbr.remove(index, length)
        print(f'after remove of "{remove}" starting at {index} for a length of {length}: sbr = "{sbr}"')
    else:
        print(f'"{remove}" was not found in the string builder instance')

    # practice replace method with single character replacement
    sbr = StringBuilder('abcd' * 3)
    print(f'sbr = "{sbr}"')
    find = 'b'
    replace = 'B'
    sbr.replace(find,replace)
    print(f'After replacing "{find}" with "{replace}", sbr = "{sbr}"')

    # practice replace method with multi-character replacement
    find = 'cd'
    replace = 'CD'
    sbr.replace(find, replace)
    print(f'After replacing "{find}" with "{replace}", sbr = "{sbr}"')

    print(f'{sbr=}')

if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()
