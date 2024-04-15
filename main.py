#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""main.py

Driving code to check the python scripts.
"""


# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled


import logging
import sys
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


        print()

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

            # check for encoding in second line of python file
            encodings = ["utf-8","utf-16","utf-32","ascii","iso-8859-1","cp1252","cp437","euc-jp","shift-jis"]
            for encoding in encodings:
                if pyfile_to_check.has_encoding_declaration(encoding, pyfile_src_code):
                    print(" "*4 + "Encoding - TRUE")
                    break
                else:
                    print(" "*4 + "Encoding - FALSE")
            
            # check if a python script contains classes. If it
            # does not, then file is considered a 'module'.
            if pyfile_to_check.has_module_docstring(pyfile_src_code):
                print(" "*4 + "File has module docstring - TRUE")
            else:
                print(" "*4 + "File has module docstring - FALSE")

            # check if a file has imports
            if pyfile_to_check.has_imports(pyfile_src_code):
                print(" "*4 + "File has imports - TRUE")
            else:
                print(" "*4 + "File has imports - FALSE")

            # TODO: Everything from here downwards:
            # check if every function has a docstring
            # pyfile_to_check.extract_functions()
            # extracted_functions = pyfile_to_check.extract_functions()
            # print(extracted_functions)
            
            # example_node = ast.parse(f"def {}({}):\n    pass").body[0]
            # if pyfile_to_check.has_function_docstring(example_node):
            #     print("TRUE")
            # else:
            #     print("FALSE")

            # tree = ast.parse(pyfile_src_code)

            # for node in ast.walk(tree):
            #     if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
            #         ...
            #         # check_docstring(node)
            #         # check_type_hint(node)

            # check the style of the names
            print(pyfile_to_check.check_names(pyfile_src_code))

            #check the line length
            print(pyfile_to_check.check_line_length(pyfile_src_code))

            # check whitespaces before paranthesis
            print(pyfile_to_check.check_whitespace_before_parentheses(pyfile_src_code))


            # check the whitespaces around the assignments
            # print(pyfile_to_check.check_whitespace_around_assignment(pyfile_src_code))

            # check if the script has a main block
            print(pyfile_to_check.has_main_block(pyfile_src_code))

            # check for the correct indentation style
            print(pyfile_to_check.check_indentation_style(pyfile_src_code))


if __name__ == "__main__":

    main(*sys.argv[1:])
