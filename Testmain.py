#Necessary imports
import unittest
from mainCode import get_repositories, commit_count

class TestMethods(unittest.TestCase):

    def testCorrectName(self):
        repo = get_repositories("richkempinski")
        repo1name = repo[1]["name"]
        self.assertEqual(repo1name, "hellogitworld" )

    def testCorrectName2(self):
        repo = get_repositories("richkempinski")
        repo2name = repo[2]["name"]
        self.assertEqual(repo2name, "helloworld")

    def testCommitCount(self):
        repo = get_repositories("richkempinski")
        repo1full = repo[1]["full_name"]
        cc1 = commit_count(repo1full)
        self.assertEqual(cc1, 30)

    def testCommitCount2(self):
        repo = get_repositories("richkempinski")
        repo2full = repo[2]["full_name"]
        cc2 = commit_count(repo2full)
        self.assertEqual(cc2, 6)

    def testPrintStatement(self):
        repos = get_repositories("richkempinski")
        repo_name = repos[1]["name"]
        repo_full_name = repos[1]["full_name"]
        commit_num = commit_count(repo_full_name)
        self.assertEqual("Repo: hellogitworld | Number of commits: 30", f"Repo: {repo_name} | Number of commits: {commit_num}")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
