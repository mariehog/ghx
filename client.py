import os
import yaml
import githubapimock as api

config_path = os.path.expanduser("~/repo.yml")
settings = yaml.load(open(config_path))

org = settings["org"]
repo = settings["repo"]
username = settings["user"]
token = settings["token"]

title = "My first client issue from Python"
body = "This was created from client application"
labels = ['todo', 'help_wanted']

issue_id = api.create_issue(org, repo, username, token, title, body)

print("Created issue: " + str(issue_id))

api.set_labels(org, repo, username, token, issue_id, labels)

print("Added labels " + str(labels) + " to issue " + str(issue_id))

