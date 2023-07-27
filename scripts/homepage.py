#!/usr/bin/env python
import json
import os
import re
import requests

USERNAME = os.popen('git config user.name').read().strip()
HOMEPAGE = 'https://%s.github.io/gists' % USERNAME

url = 'https://api.github.com/repos/%s/gists' % USERNAME
data = {'homepage':HOMEPAGE}
headers = {"Authorization": "Bearer %s" % os.getenv('GITHUB_TOKEN')}
r = requests.patch(url,data=json.dumps(data),headers=headers)
r.raise_for_status()
