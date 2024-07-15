#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""TestPEPChecker.py

Unittest for the PEPChecker class.
"""

import os
import sys
import pytest
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from classes.PEPChecker import PEPChecker

@pytest.fixture
def checker():
    return PEPChecker("test_script.py")

def test_has_shebang_line(checker):
    source_code = "#!/usr/bin/env python3\n"
    assert checker.has_shebang_line(source_code)

def test_has_encoding_declaration(checker):
    source_code = "# -*- coding: utf-8 -*-\n"
    encoding = "utf-8"
    assert checker.has_encoding_declaration(encoding, source_code)

def test_has_module_docstring(checker):
    source_code = '"""Module docstring."""\n'
    assert checker.has_module_docstring(source_code)

def test_has_imports(checker):
    source_code = "import module\n"
    assert checker.has_imports(source_code)

def test_has_function_docstring(checker):
    source_code = "def func():\n    pass\n"
    assert not checker.has_function_docstring(source_code)

def test_check_args_type_hints(checker):
    source_code = "def func(arg1, arg2: int) -> str:\n    pass\n"
    assert checker.check_args_type_hints(source_code) is None

def test_check_var_type_hints(checker):
    source_code = "def func():\n    var = 10\n"
    assert checker.check_var_type_hints(source_code) is None

def test_check_return_type_hint(checker):
    source_code = "def func() -> int:\n    return 42\n"
    assert checker.check_return_type_hint(source_code) is None

def test_check_names(checker):
    source_code = "class MyClass:\n    pass\n"
    assert checker.check_names(source_code)

def test_check_line_length(checker):
    source_code = "print('This is a long line that exceeds the 79 character limit.')\n"
    assert checker.check_line_length(source_code)

def test_check_whitespace_before_parentheses(checker):
    source_code = "func (arg)\n"
    assert checker.check_whitespace_before_parentheses(source_code)

def test_check_whitespace_around_assignment(checker):
    source_code = "a = 10\n"
    assert checker.check_whitespace_around_assignment(source_code)

def test_has_main_block(checker):
    source_code = "if __name__ == '__main__':\n    pass\n"
    assert checker.has_main_block(source_code)

def test_check_indentation_style(checker):
    source_code = "def func():\n    print('Indented with 4 spaces')\n"
    assert checker.check_indentation_style(source_code)
