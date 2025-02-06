import sys
from string_builder import StringBuilder

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def main():
    sbr = StringBuilder('Start ')
    sbr.append('A ')
    sbr.append('B ')
    sbr.append('C')
    print(sbr)

if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()