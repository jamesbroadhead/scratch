#!/usr/bin/env python
"""
Given html with tables, remove all table tags, preserving the content which
existed inside them
"""
import sys

from bs4 import BeautifulSoup

def remove(soup, tagname):
    tags = soup.findAll(tagname)

    for tag in tags:
        contents = tag.contents
        parent = tag.parent

        # Destructively rips this element out of the tree
        #print 'pre-extract: {}'.format(id(tag.parent))
        tag.extract()
        #print 'post-extract: {}'.format(tag.parent)

        # the tag doesn't unset its parent?

        # ==> this is calling append on the 'old' parent
        for content in contents:
            print id(parent)
            print id(content.parent)
            print id(tag)
            #print contents
            #print len(contents)
            parent.append(content)

def main(filename):
    with open(filename) as fh:
        content = fh.read()

    html = content
    soup = BeautifulSoup(html, "lxml")
    remove(soup, 'td')

    #print soup.prettify()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise Exception('Must supply an argument')
    for arg in sys.argv[1:]:
        main(arg)
