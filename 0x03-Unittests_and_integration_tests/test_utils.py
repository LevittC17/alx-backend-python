#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import get_json


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
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
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


if __name__ == "__main__":
    unittest.main()
