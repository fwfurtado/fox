from src.fox.intrepreter.errors.parse_error import ParseError
from src.fox.intrepreter.runners.fox_runner import FoxRunner


class FileRunner(FoxRunner):
    def run_from_file(self, file_path: str):
        with open(file_path, "rb") as read_file:
            byte_array = read_file.read()

            try:
                self.run(str(byte_array, encoding="utf-8"))
            except ParseError as e:
                print(e)
                return exit(65)

    def __call__(self, file_path: str):
        return self.run_from_file(file_path)


run_file = FileRunner()
