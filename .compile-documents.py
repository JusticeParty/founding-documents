#!/usr/bin/python

import os
import re

parseContentRegex = re.compile ('([0-9]+)\. (.*)')

def compileInOrder (parentFolder, indexList):
    compiledText = ''
    
    contents = [parseContent (path) for path in os.listdir (parentFolder)]
    contents = sorted (contents, key=lambda content: content[0])
    for content in contents:
        if content[0] is 0 or content[1] is '.' or content[1] is '..':
            continue
        
        path = os.path.join (parentFolder, content[2])
        newIndexList = indexList + [content[0]]
        
        heading = '#' * len (newIndexList)
        heading += ' ' + '.'.join (map (lambda x: str(x), newIndexList))
        compiledText += '%s. %s\n\n' % (heading, content[1])
        
        if os.path.isdir (path):
            compiledText += compileInOrder (path, newIndexList)
        
        if os.path.isfile (path):
            with open (path, 'r') as f:
                compiledText += f.read () + '\n\n\n'
    
    return compiledText

def parseContent (fileOrDirectory):
    match = parseContentRegex.match (fileOrDirectory)
    if match:
        return [int (match.group (1)), stripExtension (match.group (2)), fileOrDirectory]
    else:
        return [0, stripExtension (fileOrDirectory), fileOrDirectory]

def stripExtension (file):
    return file.replace ('.txt', '')

def compileDocuments (documentsToCompile):
    for document in documentsToCompile:
        file = open (os.path.join ('_posts', '2011-12-12-' + document.replace(' ', '-') + '.md'), 'w')
        print >> file, '---'
        print >> file, 'layout: default'
        print >> file, 'title: %s' % document
        print >> file, '---'
        
        print >> file, '{{ page.title }}'
        print >> file, '================'
        
        print >> file, compileInOrder (document, [])

compileDocuments (['Bylaws', 'Values'])
