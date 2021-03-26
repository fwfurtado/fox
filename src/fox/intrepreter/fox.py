from fox.intrepreter.runners.file_runner import run_file
from fox.intrepreter.runners.repl_runner import repl


def main(args):
    if len(args) > 1:
        print("Usage: fox [script]")
        exit(64)
    elif args:
        script_file = args[0]
        run_file(script_file)
    else:
        repl()
