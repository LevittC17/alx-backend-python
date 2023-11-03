#!/usr/bin/env python3

"""
Testing GithubOrgClient.org method to ensure
it constructs the correct URL and calls get_json
with the expected argument
"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test the GithubClient.org method
        Args:
            org_name (str): Name of the organization to test
            mock_get_json (MagicMock): Mock object for get_json
        """
        client = GithubOrgClient(org_name)

        # Perform the test without making an actual HTTP call
        client.org()

        # Assert that get_json is called once with expected arg
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        Test GithubOrgClient.public_repos_url property
        Args:
            mock_org (MagicMock): Mock object for org method
        Returns: None
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            # Create a payload dictionary
            payload = {"repos_url": "World"}

            # Set return value of the property to the payload
            mock_org.return_value = payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient('test')

            # Get the _public_repos_url property
            result = client._public_repos_url

            # Assert that the result matches the payload value
            self.assertEqual(result, payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
