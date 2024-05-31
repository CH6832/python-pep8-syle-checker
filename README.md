# PEP Checker

## :newspaper: About the project

This tool is a Python script designed to help maintain code quality and adherence to coding standards, particularly the [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/). It scans Python source files within a project directory and provides feedback on areas where code may deviate from PEP conventions.

### Content overview

    .
    ├── logs/ - implementation and test case of linked list
    ├── tests/ - implementation and test case of stack
    ├── COPYRIGHT - project copyright
    ├── LICENSE - license file
    ├── example_usages.py - main program contains example usages
    ├── PEPChecker.py - main program contains example usages
    ├── README.md - project descriptions and instructions
    └── requirements.txt - project requirements

## :notebook: Features

* PEP 8 Compliance: FileChecker evaluates Python files against the PEP 8 style guide, highlighting areas of non-compliance such as improper indentation, naming conventions, whitespace usage, and line length violations.
* Output Reports: FileChecker generates detailed reports listing detected issues, along with line numbers and descriptions, making it easy for developers to locate and address violations.
* Integration with Continuous Integration: FileChecker can be integrated into continuous integration pipelines to automatically check code quality on each commit, ensuring consistent adherence to coding standards across the project.

## :runner: Getting started

### Prerequisites and example usage

0. Clone the repository:

```sh
git clone https://github.com/CH6832/python-pep8-syle-checker.git
```

1. Navigate into root directory:

```sh
cd python-pep8-syle-checker
```

3. Install requirements:

```sh
pip3 install -r requirements.txt
```

4. Run script to see how it works:

```sh
python main.py "tests\\test_script.py"
```

5. Output can be found in `logs\` folder. Here an example output:

```
----------------------------------------------------------------------------------
Checking file: tests\test_script.py
----------------------------------------------------------------------------------
'tests\test_script.py' exists as a file.
'tests\test_script.py' is a .py file.
Starting analyzation...
    Checking type hints for args...
        Argument 'n' in function 'fibonacci' is missing type hint.
    Checking type hints for args...
        Argument 'self' in function '__init__' is missing type hint.
        Argument 'name' in function '__init__' is missing type hint.
    Checking type hints for args...
        Argument 'self' in function 'area' is missing type hint.
    Checking indentation...
        Incorrect indentation at line 15: 6 spaces instead of a multiple of 4.
    Checking lines...
        Line 3 is longer than 79 characters.
    Checking naming conventions...
    Checking return type hints...
    Checking variables type hints in function body...
    Checking variables type hints in function body...
    Checking variables type hints in function body...
    Checking for whitespace around assignment...
    Checking for single whitespace in front of bracket...
    Checking for encoding...
    Checking function docstrings...
    Checking function docstrings...
    Checking function docstrings...
        Function 'area' is missing a docstring.
    Checking the imports...
        The file does not contain import statements.
    Checking main block...
        'if __name__ == "__main__":' block in the script.
    Checking if module contains docstring...
        The module is missing a docstring.
    Checking for Shebang line...
```

## :books: Resources used to create this project

* Python
  * [Python 3.12 documentation](https://docs.python.org/3/)
  * [Built-in Functions](https://docs.python.org/3/library/functions.html)
  * [Python Module Index](https://docs.python.org/3/py-modindex.html)
  * [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
  * [ast — Abstract Syntax Trees](https://docs.python.org/3/library/ast.html)
  * [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
  * [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* Markdwon
  * [Basic syntax](https://www.markdownguide.org/basic-syntax/)
  * [Complete list of github markdown emofis](https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia)
  * [Awesome template](http://github.com/Human-Activity-Recognition/blob/main/README.md)
  * [.gitignore file](https://git-scm.com/docs/gitignore)
* Editor
  * [Visual Studio Code](https://code.visualstudio.com/)

## :bookmark: License

This project is licensed under the terms of the [MIT License](LICENSE).

## :copyright: Copyright

See the [COPYRIGHT](COPYRIGHT) file for copyright and licensing details.
