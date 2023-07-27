#!/usr/bin/env python
import json
import os
import re

USERNAME = os.popen('git config user.name').read().strip()
lines = [
    'tag|gists',
    '-|-'
]
counter = {}
for d in json.load(open('/tmp/data.json')):
    tags = re.findall(r"#(\w+)",d.get('description','') or '')
    for tag in tags:
        counter[tag]=counter.get(tag,0)+1
for tag in sorted(list(counter.keys())):
    count = counter[tag]
    url = 'https://gist.github.com/search?q=user%%3A%s+%s' % (USERNAME,tag)
    rows = [
        '[#%s](%s)' % (tag,url),
        str(count)
    ]
    lines.append('|'.join(rows))
open('tags.md','w').write("\n".join(lines))
