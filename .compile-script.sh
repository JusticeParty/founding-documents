#!/bin/bash

git config user.email "travis@justicepartyofpa.org"
git config user.name "Travis Automation"
git config remote.origin.url "git@github.com:JusticeParty/founding-documents.git"

# hack the ssh config file so we can push
cp ~/.ssh/config ~/.ssh/config.bak
echo "Host github.com" > ~/.ssh/config
echo "    StrictHostKeyChecking no" >> ~/.ssh/config

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

# unhack the ssh config file
cp ~/.ssh/config.bak ~/.ssh/config
