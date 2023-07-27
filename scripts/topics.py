#!/usr/bin/env python
import json
import os
import re
import requests

"""
https://docs.github.com/ru/rest/repos/repos?apiVersion=2022-11-28#replace-all-repository-topics
"""

USERNAME = os.popen('git config user.name').read().strip()

tags = []
for d in json.load(open('/tmp/data.json')):
    tags+= re.findall(r"#(\w+)",d.get('description','') or '')

url = 'https://api.github.com/repos/%s/gists/topics' % USERNAME
data = {"names":list(sorted(set(tags)))}
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer %s" % os.getenv('GITHUB_TOKEN'),
    "X-GitHub-Api-Version": "2022-11-28"
}
r = requests.put(url,data=json.dumps(data),headers=headers)
r.raise_for_status()
