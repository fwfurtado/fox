from src.fox.intrepreter.errors.parse_error import ParseError
from src.fox.intrepreter.runners.fox_runner import FoxRunner


class ReplRunner(FoxRunner):
    def run_repl(self):
        while True:

            line = input("> ")

            if not line:
                continue

            if line == "exit":
                return exit(0)
            try:
                self.run(line)
            except ParseError:
                ...

    def __call__(self):
        return self.run_repl()


repl = ReplRunner()
