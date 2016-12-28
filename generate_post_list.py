#! /usr/bin/env python
import json
import os

mypath = 'posts'
target_file = 'posts.json'

def getfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return a

onlyfiles = getfiles(mypath)

for (idx, val) in enumerate(onlyfiles):
  onlyfiles[idx] = mypath + '/' + onlyfiles[idx].replace('.md','')

#print json.dumps(onlyfiles)
with open(target_file, 'w') as outfile:
  json.dump(onlyfiles, outfile)

os.system("git add " + target_file)
