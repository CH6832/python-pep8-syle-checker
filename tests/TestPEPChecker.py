#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""TestPEPChecker.py

Unittest for the PEPChecker class.
"""

import os
import sys
import unittest
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from classes.PEPChecker import PEPChecker

class TestPEPChecker(unittest.TestCase):

    def setUp(self):
        self.checker = PEPChecker("test_script.py")

    def test_has_shebang_line(self):
        source_code = "#!/usr/bin/env python3\n"
        self.assertTrue(self.checker.has_shebang_line(source_code))

    def test_has_encoding_declaration(self):
        source_code = "# -*- coding: utf-8 -*-\n"
        encoding = "utf-8"
        self.assertTrue(self.checker.has_encoding_declaration(encoding, source_code))

    def test_has_module_docstring(self):
        source_code = '"""Module docstring."""\n'
        self.assertTrue(self.checker.has_module_docstring(source_code))

    def test_has_imports(self):
        source_code = "import module\n"
        self.assertTrue(self.checker.has_imports(source_code))

    def test_has_function_docstring(self):
        source_code = "def func():\n    pass\n"
        self.assertFalse(self.checker.has_function_docstring(source_code))

    def test_check_args_type_hints(self):
        source_code = "def func(arg1, arg2: int) -> str:\n    pass\n"
        self.assertIsNone(self.checker.check_args_type_hints(source_code))

    def test_check_var_type_hints(self):
        source_code = "def func():\n    var = 10\n"
        self.assertIsNone(self.checker.check_var_type_hints(source_code))

    def test_check_return_type_hint(self):
        source_code = "def func() -> int:\n    return 42\n"
        self.assertIsNone(self.checker.check_return_type_hint(source_code))

    def test_check_names(self):
        source_code = "class MyClass:\n    pass\n"
        self.assertTrue(self.checker.check_names(source_code))

    def test_check_line_length(self):
        source_code = "print('This is a long line that exceeds the 79 character limit.')\n"
        self.assertTrue(self.checker.check_line_length(source_code))

    def test_check_whitespace_before_parentheses(self):
        source_code = "func (arg)\n"
        self.assertTrue(self.checker.check_whitespace_before_parentheses(source_code))

    def test_check_whitespace_around_assignment(self):
        source_code = "a = 10\n"
        self.assertTrue(self.checker.check_whitespace_around_assignment(source_code))

    def test_has_main_block(self):
        source_code = "if __name__ == '__main__':\n    pass\n"
        self.assertTrue(self.checker.has_main_block(source_code))

    def test_check_indentation_style(self):
        source_code = "def func():\n    print('Indented with 4 spaces')\n"
        self.assertTrue(self.checker.check_indentation_style(source_code))

if __name__ == "__main__":
    unittest.main()
