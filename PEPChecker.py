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
        """    Check if the script starts with a shebang line.
        
        Keyword arguments:
        source_code -- Python source code in plain text.
        """
        print("    Checking for Shebang line...")
        lines = source_code.split("\n")
        if not lines[0].startswith("#!"):
            print(f"        The script is missing a shebang line.")
            # print(f"    The script starts with a shebang line.")


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
        print("    Checking for encoding...")
        lines = source_code.split("\n")
        if encoding in lines[1]:
            print(f"        The script has encoding declaration for '{encoding}'.")
        
            

    def has_module_docstring(self, source_code: str) -> bool:
        """Check if module contains a docstring.
        
        Keyword arguments:
        source_code -- Python source code in plain text.
        """
        print("    Checking if module contains docstring...")
        lines = source_code.split("\n")
        for line in lines:
            line = line.strip()
            # Docstrings should start with """ or '''.
            if line.startswith('"""') or line.startswith("'''"):
                # print("        The module contains a docstring.")
                continue
        print("        The module is missing a docstring.")


    def has_imports(self, source_code: str):
        """Check if a Python file contains import statements.

        Keyword arguments:
        file_path -- The path to the Python file.
        """
        print("    Checking the imports...")
        lines = source_code.split("\n")
        for line in lines:
            if line.strip().startswith("import ") or line.strip().startswith("from "):
                # print("The file contains import statements.")
                # return "Imports found"
                continue
        print("        The file does not contain import statements.")


    def has_function_docstring(self, node) -> None:
        """Check if a node has a docstring."""
        print("    Checking function docstrings...")
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
            if not (node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str)):
                print(f"        Function '{node.name}' is missing a docstring.")
        return None


    def check_args_type_hints(self, node):
        """Check if all variables and arguments in a node are type hinted."""
        # Check arguments
        print("    Checking type hints for args...")
        for arg in node.args.args:
            if not arg.annotation:
                print(f"        Argument '{arg.arg}' in function '{node.name}' is missing type hint.")


    def check_var_type_hints(self, node):
        # Check variables in function body
        print("    Checking variables type hints in function body...")
        for var in node.body:
            if isinstance(var, ast.Assign):
                for target in var.targets:
                    if isinstance(target, ast.Name): # and not target.annotation:
                        print(f"         Variable '{target.id}' in function '{node.name}' is missing type hint.")


    def check_return_type_hint(self, node):
        # Check return type hint
        print("    Checking return type hints...")
        if hasattr(node, 'returns') and not node.returns:
            print(f"        Function '{node.name}' is missing return type hint.")


    def check_names(self, source_code):
        """Check if all function, variable names, and class names follow the correct style."""
        print("    Checking naming conventions...")
        tree = ast.parse(source_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                    print(f"        Function name '{node.name}' does not follow the style 'function_name'.")
                else:
                    continue
                    # print(f"    Function name '{node.name}' does follow the style 'function_name'.")
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if not re.match(r'^[a-z_][a-z0-9_]*$', target.id):
                            print(f"        Variable name '{target.id}' does not follow the style 'variable_name'.")
                        else:
                            continue
                            # print(f"    Variable name '{target.id}' does follow the style 'variable_name'.")

            elif isinstance(node, ast.ClassDef):
                if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                    print(f"        Class name '{node.name}' does not follow the camel case style.")
                else:
                    continue
                    # print(f"    Class name '{node.name}' follow the camel case style.")


    def check_line_length(self, source_code):
        """Check if every single line is not longer than 79 characters."""
        print("    Checking lines...")
        lines = source_code.split("\n")
        for i, line in enumerate(lines):
            if len(line) <= 79:
                continue
            else:
                print(f"        Line {i+1} is longer than 79 characters.")


    def check_whitespace_before_parentheses(self, source_code):
        """Check if there are no additional whitespaces before an opening parenthesis."""
        print("    Checking for single whitespace in front of bracket...")
        lines = source_code.split("\n")
        for i, line in enumerate(lines):
            if re.search(r'\(\s', line):
                print(f"        Whitespace before opening parenthesis on line {i+1}")
            else:
                continue
                # print(f"    No whitespace before opening parenthesis on line {i+1}")


    def check_whitespace_around_assignment(self, source_code):
        """Check if there is only a single whitespace before and after a '=' symbol,
        except for keyword arguments and default values for unannotated function parameters."""
        print("    Checking for whitespace around assignment...")
        tree = ast.parse(source_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Get default values for function parameters
                defaults = [arg.default for arg in node.args.defaults]
                for i, arg in enumerate(node.args.args):
                    if i < len(defaults):
                        default_value = defaults[i]
                    else:
                        default_value = None

                    if default_value is not None:
                        if isinstance(default_value, ast.NameConstant) and default_value.value is None:
                            continue
                        if not isinstance(default_value, ast.NameConstant) and arg.annotation is None:
                            continue
                    else:
                        continue

                    if arg.annotation is not None:
                        continue

                    line_num = node.lineno
                    for child_node in ast.walk(node):
                        if isinstance(child_node, ast.Assign) and child_node.lineno == line_num:
                            for target in child_node.targets:
                                if isinstance(target, ast.Name) and target.id == arg.arg:
                                    line = source_code.split("\n")[line_num - 1]
                                    if re.search(r'\s+=\s+', line):
                                        print(f"        Additional whitespace around '=' symbol for default value of parameter '{arg.arg}' on line {line_num}")
                                    else:
                                        print(f"        No additional whitespace around '=' symbol for default value of parameter '{arg.arg}' on line {line_num}")
                                    break


    def has_main_block(self, source_code) -> None:
        """Check if the script contains if __name__ == "__main__": block."""
        print("    Checking main block...")
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
            print("        Missing 'if __name__ == \"__main__\":' block in the script.")
        else:
            print("        'if __name__ == \"__main__\":' block in the script.")


    def check_indentation_style(self, source_code):
        """Check if indentation follows the style of 4 whitespaces per indentation level."""
        print("    Checking indentation...")
        lines = source_code.split("\n")
        for i, line in enumerate(lines):
            num_spaces = len(line) - len(line.lstrip())
            if num_spaces % 4 == 0:
                continue
            else:
                print(f"        Incorrect indentation at line {i+1}: {num_spaces} spaces instead of a multiple of 4.")
