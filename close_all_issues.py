import os
import yaml
import githubapimock as api

config_path = os.path.expanduser("~/repo.yml")
settings = yaml.load(open(config_path))

org = settings["org"]
repo = settings["repo"]
username = settings["user"]
token = settings["token"]

all_issues = api.get_issues(org, repo, username, token)
for issue in all_issues:
    number = issue["number"]
    api.close_issue(org, repo, username, token, number)
    print("Closing issue: " + str(number))

#    print(number)

# issue = all_issues[0]
# number = issue['number']
# print(number)

