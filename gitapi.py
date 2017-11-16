from github import Github
import sys

#Github instance:
g = Github(sys.argv[1],sys.argv[2])

for repo in g.get_user().get_repos():
    print repo.name
