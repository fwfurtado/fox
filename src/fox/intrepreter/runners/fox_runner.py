from src.fox.intrepreter.lexical.lexical_scanner import Scanner


class FoxRunner:
    def run(self, source: str):
        for token in Scanner(source):
            print(token)
