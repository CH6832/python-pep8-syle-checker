#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""main.py

Driving code to check the python scripts.
"""


# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled


import ast
import logging
import sys
import inspect
import os
from PEPChecker import PEPChecker


def main(*args):
    """main program
    
    TODO: Add logging, profiling, optimiatzation, tests
    """

    # check if arguments provided
    if not args:
        print("No arguments provided.")
        return 1

    for filepath in args:
        
        # TODO:
        # Configure logging
        logging.basicConfig(filename=f"logs/{os.path.basename(filepath)}.log".replace(".py",""), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        # # Log some messages
        # logging.debug('This is a debug message')    # Won't be shown by default because the logging level is set to INFO
        # logging.info('This is an informational message')
        # logging.warning('This is a warning message')
        # logging.error('This is an error message')
        # logging.critical('This is a critical message')

        # print()

        # check if the filepath is valid and the file exists
        if os.path.isfile(filepath):
            logging.info(f"{filepath} exists as a file.")
        else:
            logging.info(f"{filepath} does not exist as a file.")
            sys.exit(1)
        
        print()

        # check if file is a .py script
        if filepath.endswith(".py"):
            logging.info(f"'{filepath}' is a .py file.")
        else:
            logging.info(f"'{filepath}' is a .py file.")
            sys.exit(1)

        print()

        with open(filepath, "r", encoding="utf-8") as file:

            # initialize the class with filepath
            pyfile_to_check: PEPChecker = PEPChecker(filepath)

            # read the content of the python file
            pyfile_src_code: str = file.read()

            # beginn file chekcing
            print(f"Checking file '{filepath}'")

            if pyfile_to_check.has_shebang_line(pyfile_src_code):
                print(" "*4 + "Shebang line - TRUE")
            else:
                print(" "*4 + "Shebang line - FALSE")

            # Create an instance of the class
            # my_instance = MyClass()

            # Get all methods defined within the class
            methods = [method for method_name, method in inspect.getmembers(pyfile_to_check, predicate=inspect.ismethod)]

            # Call the methods one after another with an argument
            arg_value = "example_argument"
            for method in methods:
                if "has_encoding_declaration" in method.__name__:
                    encodings = ["utf-8","utf-16","utf-32","ascii","iso-8859-1","cp1252","cp437","euc-jp","shift-jis"]
                    for encoding in encodings:
                        if method(encoding, pyfile_src_code):
                            print(" "*4 + "Encoding - TRUE")
                            break
                        else:
                            print(" "*4 + "Encoding - FALSE")

                elif "has_function_docstring" in method.__name__ or "has_function_docstring" in method.__name__ or "check_return_type_hints" in method.__name__:
                    tree = ast.parse(pyfile_src_code)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                            method(node)
                            method(node)
                else:
                    method(pyfile_src_code)

if __name__ == "__main__":
    main(*sys.argv[1:])
