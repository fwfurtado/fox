from fox.intrepreter.scanners.scanner import Scanner


class FoxRunner:

    def run(self, source: str):
        for token in Scanner(source):
            print(token)