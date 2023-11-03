#!/usr/bin/env python3

"""
Testing GithubOrgClient.org method to ensure
it constructs the correct URL and calls get_json
with the expected argument
"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock, call
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test methods defined here"""
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

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test the GithubOrgClient.public_repos method
        Args:
          repos_url (PropertyMock): Mock _public_repos_url
          mock_get_json (MagicMock): Mock object for get_json
        Return: None
        """
        mock_public_repos_url.return_value = "hello/world"

        # Mock get_json to return a custom payload
        mock_get_json.return_value = [
            {"name": "Google"},
            {"name": "Twitter"}
        ]

        # Create an instance of GithubOrgClient
        test_class = GithubOrgClient('test')

        # Call the public_repos method
        result = test_class.public_repos()

        # Assert that the list of repos matches the expected value
        expected_repos = ["Google", "Twitter"]
        self.assertEqual(result, expected_repos)

        # Assert that the mocked property and get_json were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test GithubOrgClient.has_license method with parameterized inputs
        Args:
            repo: Input repository with a license key
            license_key: License key to check
            expected_result: Expected
        """
        test_class = GithubOrgClient('test')

        # Call the has_license method
        result = test_class.has_license(repo, license_key)

        # Assert that result matches the expected value
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
