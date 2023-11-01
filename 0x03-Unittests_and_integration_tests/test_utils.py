#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    A test class for the access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path,
                               expected_result):
        """
        Test the access_nested_method function with various inputs
        Args:
            nested_map (dict): The nested map to access
            path (tuple): The path to follow in the map
            expected_result: The expected result for the function
        """
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_result)


if __name__ == "__main__":
    unittest.main()
