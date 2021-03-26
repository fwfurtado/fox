class FoxError(RuntimeError):

    def __init__(self, line: int, where: str, message: str):
        self.__line = line
        self.__where = where
        self.__message = message

    @property
    def line(self):
        return self.__line

    @property
    def where(self):
        return self.__where

    @property
    def message(self):
        return self.__message

