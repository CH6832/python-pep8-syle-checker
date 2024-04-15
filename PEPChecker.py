#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""PEPChecker.py

The files contains the PEP8Checker class and relevant functions to check
if a script is styled according to the 'Python Enhancement Proposal 8 - Style Guide for Python Code'
The style guide can be found in https://peps.python.org/pep-0008/.
"""


# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled


import ast
import re
from typing import List


class PEPChecker:
    """A class to check if a Python script adheres to PEP style guidelines."""


    def __init__(self, filepath_to_py_script: str) -> None:
        """Initialize the PEPChecker class.
        
        Keyword arguemnts:
        filepath_to_py_script -- Path to pythonscript that should be checked.
        """
        self.filepath_to_py_script = filepath_to_py_script
        return None


    def has_shebang_line(self, source_code: str) -> bool:
        """Check if the script starts with a shebang line.
        
        Keyword arguments:
        source_code -- Python source code in plain text.
        """
        lines: List[str] = source_code.split("\n")
        if not lines[0].startswith("#!"):
            return False
        else:
            return True


    def has_encoding_declaration(self, encoding: str, source_code: str) -> bool:
        """Check if the script contains relevant encoding.
        
        Keyword arguments:
        source_code -- Python source code in plain text.        
        
        Notes:
        Some example encodings:
        # -*- coding: utf-8 -*-
        # -*- coding: utf-16 -*-
        # -*- coding: utf-32 -*-
        # -*- coding: ascii -*-
        # -*- coding: iso-8859-1 -*-
        # -*- coding: cp1252 -*-
        # -*- coding: cp437 -*-
        # -*- coding: euc-jp -*-
        # -*- coding: shift-jis -*-
        """
        lines: List[str] = source_code.split("\n")
        if not encoding in lines[1]:
            return False
        else:
            return True


    def has_module_docstring(self, source_code: str) -> bool:
        """Check if module contains a docstring.
        
        Keyword arguments:
        source_code -- Python source code in plain text.

        TODO: Function not working correct. Pls fix
        """
        # lines: List[str] = source_code.split("\n")
        # for line in lines:
        #     line = line.strip()
        #     # docstrings should start with """ but it can be ''' as well
        #     if line.startswith('"""') or line.startswith("'''"):
        #         return True
        #     else:
        #         return False
        return any(line.strip().startswith('"""') or line.strip().startswith("'''") for line in source_code.split("\n"))


    def has_imports(self, source_code: str) -> bool:
        """Check if a Python file contains import statements.

        Keyword arguments:
        file_path -- The path to the Python file.
        """
        lines: List[str] = source_code.split("\n")
        for line in lines:
            if line.strip().startswith("import ") or line.strip().startswith("from "):
                return True
        return False


    def extract_functions(self) -> None:
        """Extract all function definitions from a Python script."""
        file = open(self.filepath_to_py_script, "r")
        tree = ast.parse(file.read(), filename=self.filepath_to_py_script)
        # with open(self.filepath_to_py_script, "r") as file:
        #    tree = ast.parse(file.read(), filename=self.filepath_to_py_script)
            
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                function_info = {
                    'name': node.name,
                    'parameters': [arg.arg for arg in node.args.args],
                    'type_hints': {},
                    'body': ast.get_source_segment(file.readlines(), node.body)
                }

                # Extract type hints
                for arg in node.args.args:
                    if arg.annotation:
                        function_info['type_hints'][arg.arg] = ast.get_source_segment(file.readlines(), arg.annotation)

                print(function_info)

        return None


    def has_function_docstring(self, node) -> None:
        """Check if a node has a docstring."""
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
            if not (node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str)):
                print(f"Function '{node.name}' is missing a docstring.")
        return None


    # TODO:
    # def check_type_hints(self, node):
    #     """Check if all variables and arguments in a node are type hinted."""
    #     for arg in node.args.args:
    #         if not arg.annotation:
    #             print(f"Argument '{arg.arg}' in function '{node.name}' is missing type hint.")
        
    #     for var in node.body:
    #         if isinstance(var, ast.Assign):
    #             for target in var.targets:
    #                 if isinstance(target, ast.Name) and not target.annotation:
    #                     print(f"Variable '{target.id}' in function '{node.name}' is missing type hint.")



    def check_names(self, source_code):
        """Check if all function, variable names, and class names follow the correct style."""
        tree = ast.parse(source_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                    print(f"Function name '{node.name}' does not follow the style 'function_name'.")
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if not re.match(r'^[a-z_][a-z0-9_]*$', target.id):
                            print(f"Variable name '{target.id}' does not follow the style 'variable_name'.")
            elif isinstance(node, ast.ClassDef):
                if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                    print(f"Class name '{node.name}' does not follow the camel case style.")


    def check_line_length(self, source_code):
        """Check if every single line is not longer than 79 characters."""
        lines = source_code.split("\n")
        for i, line in enumerate(lines):
            if len(line) > 79:
                print(f"Line {i+1} is longer than 79 characters.")


    def check_whitespace_before_parentheses(self, source_code):
        """Check if there are no additional whitespaces before an opening parenthesis."""
        lines = source_code.split("\n")
        for i, line in enumerate(lines):
            if re.search(r'\(\s', line):
                print(f"Whitespace before opening parenthesis on line {i+1}")


    # TODO:
    # def check_whitespace_around_assignment(self, source_code):
    #     """Check if there is only a single whitespace before and after a '=' symbol,
    #     except for keyword arguments and default values for unannotated function parameters."""
    #     tree = ast.parse(source_code)
    #     for node in ast.walk(tree):
    #         if isinstance(node, ast.FunctionDef):
    #             # Get default values for function parameters
    #             defaults = [arg.default for arg in node.args.args]
    #             for i, arg in enumerate(node.args.args):
    #                 if isinstance(defaults[i], ast.NameConstant) and defaults[i].value is None:
    #                     # If the default value is None (indicating no default value)
    #                     # and the argument is not type annotated, continue to the next argument
    #                     continue
    #                 if not isinstance(defaults[i], ast.NameConstant) and arg.annotation is None:
    #                     # If the default value is not a name constant (indicating a non-None default value)
    #                     # and the argument is not type annotated, continue to the next argument
    #                     continue
    #                 if arg.annotation is not None:
    #                     # If the argument is type annotated, we should allow whitespace around '=' symbol
    #                     continue
    #                 # Otherwise, check for whitespace around '=' symbol
    #                 line_num = node.lineno
    #                 for child_node in ast.walk(node):
    #                     if isinstance(child_node, ast.Assign) and child_node.lineno == line_num:
    #                         for target in child_node.targets:
    #                             if isinstance(target, ast.Name) and target.id == arg.arg:
    #                                 # We found the assignment of the parameter's default value
    #                                 line = source_code.split("\n")[line_num - 1]
    #                                 if re.search(r'\s+=\s+', line):
    #                                     print(f"Additional whitespace around '=' symbol for default value of parameter '{arg.arg}' on line {line_num}")
    #                                 break



    def has_main_block(self, source_code) -> None:
        """Check if the script contains if __name__ == "__main__": block."""
        tree = ast.parse(source_code)
        main_block_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                if (isinstance(node.test, ast.Compare) and
                    isinstance(node.test.left, ast.Name) and
                    node.test.left.id == "__name__" and
                    len(node.test.ops) == 1 and
                    isinstance(node.test.ops[0], ast.Eq) and
                    isinstance(node.test.comparators[0], ast.Str) and
                    node.test.comparators[0].s == "__main__"):
                    main_block_found = True
                    break
        
        if not main_block_found:
            print("Missing 'if __name__ == \"__main__\":' block in the script.")


    def check_indentation_style(self, source_code):
        """Check if indentation follows the style of 4 whitespaces per indentation level."""
        lines = source_code.split("\n")
        for i, line in enumerate(lines):
            num_spaces = len(line) - len(line.lstrip())
            if num_spaces % 4 != 0:
                print(f"Incorrect indentation at line {i+1}: {num_spaces} spaces instead of a multiple of 4.")
