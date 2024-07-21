#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""style_checker.py

Driving code to check the python scripts.
"""

# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled

import ast
import sys
import inspect
import os
from classes.PEPChecker import PEPChecker

def main(*args):
    """Driving code."""

    if not args:
        print("No arguments provided!")
        return 1

    for filepath in args:

        with open('logs/' + os.path.basename(filepath.replace(".py","")) + '_analyzation_result.txt', 'w', encoding="utf-8") as f:
            
            original_stdout = sys.stdout

            sys.stdout = f            

            print(f"""\n----------------------------------------------------------------------------------
Checking file: {filepath}
----------------------------------------------------------------------------------""")

            # check if the filepath is valid and the file exists
            if os.path.isfile(filepath):
                print(f"'{filepath}' exists as a file.")
            else:
                print(f"'{filepath}' does not exist as a file.")
                sys.exit(1)
            
            # check if file is a .py script
            if filepath.endswith(".py"):
                print(f"'{filepath}' is a .py file.")
            else:
                print(f"'{filepath}' is a .py file.")
                sys.exit(1)

            with open(filepath, "r", encoding="utf-8") as file:

                # initialize the class with filepath
                pyfile_to_check: PEPChecker = PEPChecker(filepath)

                # read the content of the python file
                pyfile_src_code: str = file.read()

                print("Starting analyzation...")

                # get all methods within class
                methods = [method for method_name, method in inspect.getmembers(pyfile_to_check, predicate=inspect.ismethod)]

                # call methods one after another
                for method in methods:
                    if "has_encoding_declaration" in method.__name__:
                        encodings = ["utf-8","utf-16","utf-32","ascii","iso-8859-1","cp1252","cp437","euc-jp","shift-jis"]
                        for encoding in encodings:
                            if not method(encoding, pyfile_src_code):
                                break

                    elif "has_function_docstring" in method.__name__ or "has_function_docstring" in method.__name__ or "check_return_type_hints" in method.__name__ or "check_args_type_hints" in method.__name__ or "check_var_type_hints" in method.__name__:
                        tree = ast.parse(pyfile_src_code)
                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                                method(node) 
                    else:
                        method(pyfile_src_code)

            sys.stdout = original_stdout

    return 0

if __name__ == "__main__":
    main(*sys.argv[1:])
