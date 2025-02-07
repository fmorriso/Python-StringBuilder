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
    print(sbr)


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()
