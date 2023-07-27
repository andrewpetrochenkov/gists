#!/usr/bin/env python
import json
import os
import requests


USERNAME = os.popen('git config user.name').read().strip()
data = []
headers = {"Authorization": "Bearer %s" % os.getenv('GITHUB_TOKEN')}
page = 1
while True:
    url = 'https://api.github.com/users/%s/gists?per_page=100&page=%s' % (USERNAME,page)
    r = requests.get(url,headers=headers)
    print('%s %s' % (url,r.status_code))
    if r.status_code == 200:
        data+=list(filter(lambda d:d['public'],r.json()))
        page+=1
        if '"next"' not in str(r.headers.get('Link','')):
            break
    else:
        break
open('/tmp/data.json','w').write(json.dumps(data, indent=4))
