import unittest
from PEPChecker import PEPChecker

class TestPEPChecker(unittest.TestCase):
    def setUp(self):
        self.pep_checker = PEPChecker("test_script.py")

    def test_has_shebang_line(self):
        source_code_with_shebang = "#!/usr/bin/env python\nprint('Hello, world!')"
        source_code_without_shebang = "print('Hello, world!')"
        
        self.assertTrue(self.pep_checker.has_shebang_line(source_code_with_shebang))
        self.assertFalse(self.pep_checker.has_shebang_line(source_code_without_shebang))

    def test_has_encoding_declaration(self):
        source_code_with_encoding = "# -*- coding: utf-8 -*-\nprint('Hello, world!')"
        source_code_without_encoding = "print('Hello, world!')"
        
        self.assertTrue(self.pep_checker.has_encoding_declaration('utf-8', source_code_with_encoding))
        self.assertFalse(self.pep_checker.has_encoding_declaration('utf-8', source_code_without_encoding))

    def test_has_module_docstring(self):
        source_code_with_docstring = '"""This is a module docstring."""\nprint("Hello, world!")'
        source_code_without_docstring = 'print("Hello, world!")'
        
        self.assertTrue(self.pep_checker.has_module_docstring(source_code_with_docstring))
        self.assertFalse(self.pep_checker.has_module_docstring(source_code_without_docstring))

    def test_has_imports(self):
        source_code_with_imports = "import math\nprint(math.pi)"
        source_code_without_imports = "print('Hello, world!')"
        
        self.assertTrue(self.pep_checker.has_imports(source_code_with_imports))
        self.assertFalse(self.pep_checker.has_imports(source_code_without_imports))

    # Add more test methods for other PEP checking functions

    def test_extract_functions(self):
        # Not easy to test since it interacts with external file. You may want to refactor for better testability.
        ...

    def test_check_names(self):
        source_code_with_correct_names = "def function_name():\n\tvariable_name = 5\n\nclass ClassName:\n\tpass"
        source_code_with_incorrect_function_name = "def functionName():\n\tpass"
        source_code_with_incorrect_variable_name = "def function_name():\n\tVariableName = 5\n"
        source_code_with_incorrect_class_name = "class className:\n\tpass"
        
        self.assertIsNone(self.pep_checker.check_names(source_code_with_correct_names))
        self.assertIn("function_name", self.pep_checker.check_names(source_code_with_incorrect_function_name))
        self.assertIn("VariableName", self.pep_checker.check_names(source_code_with_incorrect_variable_name))
        self.assertIn("className", self.pep_checker.check_names(source_code_with_incorrect_class_name))

    def test_check_line_length(self):
        source_code_with_long_line = "a" * 80
        source_code_with_short_line = "a" * 70
        
        self.assertTrue(self.pep_checker.check_line_length(source_code_with_long_line))
        self.assertFalse(self.pep_checker.check_line_length(source_code_with_short_line))

    def test_check_whitespace_before_parentheses(self):
        source_code_with_whitespace = "print ('Hello, world!')"
        source_code_without_whitespace = "print('Hello, world!')"
        
        self.assertTrue(self.pep_checker.check_whitespace_before_parentheses(source_code_with_whitespace))
        self.assertFalse(self.pep_checker.check_whitespace_before_parentheses(source_code_without_whitespace))

    def test_has_main_block(self):
        source_code_with_main_block = "if __name__ == '__main__':\n\tprint('Hello, world!')"
        source_code_without_main_block = "print('Hello, world!')"
        
        self.assertTrue(self.pep_checker.has_main_block(source_code_with_main_block))
        self.assertFalse(self.pep_checker.has_main_block(source_code_without_main_block))

    def test_check_indentation_style(self):
        source_code_with_correct_indentation = "def function():\n\tprint('Hello, world!')"
        source_code_with_incorrect_indentation = "def function():\n  print('Hello, world!')"
        
        self.assertIsNone(self.pep_checker.check_indentation_style(source_code_with_correct_indentation))
        self.assertIn("Incorrect indentation", self.pep_checker.check_indentation_style(source_code_with_incorrect_indentation))

if __name__ == '__main__':
    unittest.main()
