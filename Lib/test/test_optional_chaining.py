import ast
import unittest

class OptionalChainingSyntaxTest(unittest.TestCase):
    def test_optional_attribute_parsed(self):
        tree = ast.parse("x?.name")
        expr = tree.body[0].value
        self.assertIsInstance(expr, ast.OptionalAttribute)
        self.assertIsInstance(expr.value, ast.Name)
        self.assertEqual(expr.attr, "name")

    def test_optional_attribute_none(self):
        with self.assertRaises(SyntaxError):
            ast.parse("y?")

if __name__ == '__main__':
    unittest.main()
