#!/usr/bin/env python3

"""
unittest and integration testing
"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import get_json
from utils import memoize


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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Raise a KeyError for the respective inputs"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Test class for test_get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test the mock response object"""
        with patch('requests.get') as mock_get:
            # Create a mock response object with a json method
            mock_response = Mock()
            mock_response.json.return_value = test_payload

            # Configure the mock get method to return the mock_response
            mock_get.return_value = mock_response

            # Call the get_json function
            result = get_json(test_url)

            # Ensure that the get method was called exactly once
            # with the test_url
            mock_get.assert_called_once_with(test_url)

            # Test that the output of get_json is equal to test_payload
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """The class with test_memoize method"""
    def test_memoize(self):
        """Test the @memoize decorator"""
        class TestClass:
            """Define a class for Testing"""
            def a_method(self):
                """Test method"""
                return 42

            @memoize
            def a_property(self):
                """Memoize decorator"""
                return self.a_method()

        # Mock the a_method using patch
        with patch.object(TestClass, 'a_method') as mock_a_method:
            # Create an instance of TestClass
            instance = TestClass()

            # Call a_property twice
            instance.a_property()
            instance.a_property()

            # Assert that a_method is only called once
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
