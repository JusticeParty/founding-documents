#!/bin/bash

# when we have Travis or some other build agent working, we can do something like this:
#git config user.email "travis@justicepartyofpa.org"
#git config user.name "Travis Automation"
#git config remote.origin.url "git@github.com:JusticeParty/founding-documents.git"

cd /home/dan/projects/personal/founding-documents/

./.compile-documents.py
git add .
git commit -a -m "updating compiled documents"
git push

git checkout gh-pages
git checkout master -- _posts
git add .
git commit -a -m "updating compiled documents"
git push

git checkout master
