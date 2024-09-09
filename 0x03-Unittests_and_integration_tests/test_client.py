#!/usr/bin/env python3
"""
4. Parameterize and patch as decorators
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org"""
        mock_get_json.return_value = {"key": "value"}
        client = GithubOrgClient(org_name)

        result = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"key": "value"})

    @patch("client.GithubOrgClient.org", new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the expected repos URL."""
        mock_org.return_value = (
            {"repos_url": "https://api.github.com/orgs/test-org/repos"})

        # Create an instance of the GithubOrgClient
        client = GithubOrgClient("test-org")

        # Check if the _public_repos_url returns the correct URL
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/test-org/repos")

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=property)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test public_repos method."""
        # Define the mocked return values
        mock_public_repos_url.return_value = (
            "https://api.github.com/orgs/test-org/repos")
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        # Create an instance of the client
        client = GithubOrgClient("test-org")

        # Call the public_repos method
        repos = client.public_repos()

        # Check the result
        expected_repos = ["repo1", "repo2", "repo3"]
        self.assertEqual(repos, expected_repos)

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test-org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""
        client = GithubOrgClient("test-org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
