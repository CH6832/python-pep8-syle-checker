# PEP Checker

## :newspaper: About the project

This tool is a Python script designed to help maintain code quality and adherence to coding standards, particularly the [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/). It scans Python source files within a project directory and provides feedback on areas where code may deviate from PEP conventions.

### Content overview

    .
    ├── logs/ - implementation and test case of linked list
    ├── tests/ - implementation and test case of stack
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

1. Install requirements:

```bash
pip3 install -r requirements.txt
```

2. Run script to see how it works:

```bash
python main.py "tests\\download_raw_bb.py" "tests\\test_script.py"
```

## :books: Resources used to create this project

* Python
  * [Python 3.12.3 documentation](https://docs.python.org/3.12/)
  * [Built-in Functions](https://docs.python.org/3.12/library/functions.html)
  * [Python Module Index](https://docs.python.org/3.12/py-modindex.html)
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

[MIT License](https://opensource.org/license/mit) :copyright: 2024 Christoph Hartleb
