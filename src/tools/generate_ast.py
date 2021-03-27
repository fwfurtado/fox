from pathlib import Path

import re

TYPES = {
    "Binary": [("left", "Expr"), ("operator", "Token"), ("right", "Expr")],
    "Unary": [("left", "Expr"), ("operator", "Token")],
    "Literal": [("value", "Any")],
    "Grouping": [("expression", "Expr")],
}

PATTERN = re.compile(r"(?<!^)(?=[A-Z])")


def snake_case(text):
    return PATTERN.sub("_", text).lower()


def generate_file(output_dir, class_name, fields):
    filename = snake_case(class_name) + ".py"
    fields_str = ", ".join(
        [f"{field_name}: {field_type}" for field_name, field_type in fields]
    )
    output_file = str(Path(output_dir) / filename)

    with open(output_file, "w") as file:
        if ": Any" in fields_str:
            file.write("from typing import Any\n\n")

        if ": Token" in fields_str:
            file.write("from fox.intrepreter.tokens.token import Token\n")

        file.write(
            "from fox.intrepreter.syntax_expressions.expr import Expr, Visitor\n\n\n"
        )
        file.write(f"class {class_name}(Expr):\n")
        file.write(f"\tdef __init__(self, {fields_str}):\n")

        for field_name, _ in fields:
            file.write(f"\t\tself.__{field_name} = {field_name}\n")

        file.write("\n")

        for field_name, field_type in fields:
            file.write(f"\t@property\n")
            file.write(f"\tdef {field_name}(self) -> {field_type}:\n")
            file.write(f"\t\treturn self.__{field_name}\n\n")

        snaked_type_name = snake_case(class_name)

        file.write(
            f"\tdef accept(self, visitor: Visitor['{class_name}']) -> '{class_name}':\n"
        )
        file.write(f"\t\treturn visitor.visit_{snaked_type_name}_expr(self)")


def generate_base_file(base_dir, class_name, types):
    filename = snake_case(class_name) + ".py"
    output_file = str(Path(base_dir) / filename)

    with open(output_file, "w") as file:
        file.write("from abc import ABC, abstractmethod\n")
        file.write("from typing import TypeVar, Generic\n\n\n")

        file.write(f"T = TypeVar('T')\n\n\n")
        file.write(f"class Visitor(ABC, Generic[T]):\n\n")

        for type_name in types.keys():
            snaked_type_name = snake_case(type_name)

            file.write(f"\t@abstractmethod\n")
            file.write(
                f"\tdef visit_{snaked_type_name}_expr(self, expr: '{type_name}') -> T:\n"
            )
            file.write(f"\t\t...\n\n")

        file.write(f"\n")

        file.write(f"class {class_name}(ABC):\n\n")
        file.write(f"\t@abstractmethod\n")
        file.write(f"\tdef accept(self, visitor: Visitor[T]) -> T:\n")
        file.write(f"\t\t...\n")


if __name__ == "__main__":
    base_dir = "/src/fox/intrepreter/syntax_expressions"

    generate_base_file(base_dir, "Expr", TYPES)

    for name, params in TYPES.items():
        generate_file(base_dir, name, params)
