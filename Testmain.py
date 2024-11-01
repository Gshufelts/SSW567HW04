# Necessary imports
import unittest
from mainCode import get_repositories, commit_count
from unittest.mock import patch

class TestMethods(unittest.TestCase):

    @patch('requests.get')
    def testCorrectName(self, mock_get):
        mock_get.return_value.json.return_value = [{}, {"name": "hellogitworld"}]
        repo = get_repositories("richkempinski")
        repo1name = repo[1]["name"]
        self.assertEqual(repo1name, "hellogitworld")

    @patch('requests.get')
    def testCorrectName2(self, mock_get):
        mock_get.return_value.json.return_value = [{}, {"name": "hellogitworld"}, {"name": "helloworld"}]
        repo = get_repositories("richkempinski")
        repo2name = repo[2]["name"]
        self.assertEqual(repo2name, "helloworld")

   @patch('requests.get')
    def testCommitCount(self, mock_get):
        mock_get.side_effect = [
            Mock(json=Mock(return_value=[{"full_name": "richkempinski/hellogitworld"}])),
            Mock(json=Mock(return_value=[{}, {}] * 15))
        ]
        repo = get_repositories("richkempinski")
        repo1full = repo[0]["full_name"]
        cc1 = commit_count(repo1full)
        self.assertEqual(cc1, 30)

    @patch('requests.get')
    def testCommitCount2(self, mock_get):
        mock_get.side_effect = [
            Mock(json=Mock(return_value=[{"full_name": "richkempinski/helloworld"}])),
            Mock(json=Mock(return_value=[{}, {}] * 3))
        ]
        repo = get_repositories("richkempinski")
        repo2full = repo[0]["full_name"]
        cc2 = commit_count(repo2full)
        self.assertEqual(cc2, 6)

    @patch('requests.get')
    def testPrintStatement(self, mock_get):
        mock_get.side_effect = [
            Mock(json=Mock(return_value=[{"name": "hellogitworld", "full_name": "richkempinski/hellogitworld"}])),
            Mock(json=Mock(return_value=[{}, {}] * 15))
        ]
        repos = get_repositories("richkempinski")
        repo_name = repos[0]["name"]
        repo_full_name = repos[0]["full_name"]
        commit_num = commit_count(repo_full_name)
        self.assertEqual(f"Repo: {repo_name} | Number of commits: {commit_num}", "Repo: hellogitworld | Number of commits: 30")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
