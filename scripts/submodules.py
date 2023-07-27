#!/usr/bin/env python
import json
import subprocess

data = json.load(open('data.json'))
for d in data:
    id_shrink = '%s..%s' % (d['id'][0:2],d['id'][-2:])
    filename = list(d['files'].keys())[0]
    description = d.get('description','') or '' # todo: remove
    url = 'git@gist.github.com:%s.git' % d['id']
    path = '%s %s %s' % (id_shrink,filename,description)
    args = ['git','submodule','add',url,path]
    print(' '.join(args))
    subprocess.call(args)
