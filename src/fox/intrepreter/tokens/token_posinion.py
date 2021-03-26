class TokenPosition:

    def __init__(self, line: int, column: int, length: int):
        self.__line = line
        self.__column = column
        self.__length = length

    @property
    def line(self):
        return self.__line

    @property
    def column(self):
        return self.__column

    @property
    def length(self):
        return self.__length