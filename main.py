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
    sbr.remove(index, length)
    print(f'after remove of "{remove}" starting at {index} for a length of {length}: sbr = "{sbr.to_string()}"')

if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()
