#!/usr/bin/env python
from datetime import datetime
import json
import re
import subprocess

lines = [
    'id|file|description',
    '-|-|-'
]
for d in json.load(open('/tmp/data.json')):
    id_shrink = '%s..%s' % (d['id'][0:2],d['id'][-2:])
    filename = list(d['files'].keys())[0]
    description = (d.get('description','') or '').replace('|','\\|')
    url = 'https://gist.github.com/%s' % d['id']
    rows = [
        '[%s](%s)' % (id_shrink,url),
        '[%s](%s)' % (filename,url),
        description
    ]
    lines.append('|'.join(rows))
open('README.md','w').write("\n".join(lines))
