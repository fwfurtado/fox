class ErrorReport:

    def error(self,line: int, message: str):
        self.report(line=line, message=message)

    def report(self, line: int, message: str, where:str = "" ):
        print(f"[line {line}] Error {where} : {message}")