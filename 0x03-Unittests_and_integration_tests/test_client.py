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
<<<<<<< HEAD
    
    @patch("client.GithubOrgClient.org", new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the expected repos URL."""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test-org/repos"}

        # Create an instance of the GithubOrgClient
        client = GithubOrgClient("test-org")

        # Check if the _public_repos_url returns the correct URL
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/test-org/repos")

=======
>>>>>>> 16e38e905d43d0f0cae9a64034f58455fad901e5


if __name__ == '__main__':
    unittest.main()
