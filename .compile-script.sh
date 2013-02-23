#!/bin/bash
./.compile-documents.py
git checkout gh-pages
git checkout master -- _posts
git commit -a -m "updating compiled documents"
git checkout master
git commit -a -m "updating compiled documents"
git push
