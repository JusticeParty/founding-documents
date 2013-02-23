#!/bin/bash

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
