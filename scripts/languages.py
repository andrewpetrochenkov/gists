#!/usr/bin/env python
import json
import os
import re

data = json.load(open('/tmp/data.json'))
USERNAME = os.popen('git config user.name').read().strip()
lines = [
    'language|gists',
    '-|-'
]
counter = {}
for d in data:
    languages = list(map(lambda d:d['language'],list(d['files'].values())))
    for language in languages:
        counter[language]=counter.get(language,0)+1
for language in sorted(list(counter.keys()),key=lambda l:str(l).lower()):
    count = counter[language]
    url = 'https://gist.github.com/search?q=user%%3A%s+language:%s' % (USERNAME,str(language).replace(' ','%20'))
    rows = [
        '[%s](%s)' % (language,url),
        str(count)
    ]
    lines.append('|'.join(rows))
open('languages.md','w').write("\n".join(lines))
