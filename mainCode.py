#Importing brandprint
from BrandPrint import my_brand

#Imports for Github functions
import requests
import json

#Testable function for getting repositories
def get_repositories(username):

    #Getting url and storing json
    url = f'https://api.github.com/users/{username}/repos'
    userData = requests.get(url)

    #Returning repo as json
    return userData.json()

#Testable function for getting commit count
def commit_count(repoName):

    #Getting commits url
    url = f'https://api.github.com/repos/{repoName}/commits'
    commitsData = requests.get(url)

    #Returning amount of commits
    return len(commitsData.json())

#Main function for connecting two previous functions
def main():
    #Prompting for github username and retrieving data
    username = input("Please enter the name of the user you would like analytics on: ")
    repos = get_repositories(username)

    #Creating loop for print string
    for repo in repos:
        repo_name = repo["name"]
        repo_full_name = repo["full_name"]
        commit_num = commit_count(repo_full_name)

        print(f'Repo: {repo_name} | Number of commits: {commit_num}')

if __name__ == '__main__':
    my_brand("Homework 04a")
    main()
    my_brand("Homework 04a")
