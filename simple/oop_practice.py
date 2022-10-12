from typing import Optional

int_or_none = Optional[int]
float_or_none = Optional[int]
str_or_none = Optional[int]

class StrUtils:
    @staticmethod
    def IsEmptyOrWhitespaces(value: str) -> bool:
        return not value or value.isspace()


if __name__ == '__main__':
    def column_count(line: str) -> int_or_none:
        if StrUtils.IsEmptyOrWhitespaces(line):
            return None
        return len(line.split(","))

    print(column_count(" \n\t   "))
    print(column_count("a"))
    print(column_count("a,b"))