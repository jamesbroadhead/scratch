#!/usr/bin/env python

import sys

from bs4 import BeautifulSoup

def remove(soup, tagname):
    for tag in soup.findAll(tagname):
        contents = tag.contents
        parent = tag.parent
        tag.extract()
        for tag in contents:
            parent.append(tag)
    return soup.prettify()

def main(filename):
    with open(filename) as fh:
        content = fh.read()

    html = content
    soup = None
    for tag in [ 'td', 'tr', 'thead', 'tbody', 'ttail', 'table' ]:
        soup = BeautifulSoup(html, "lxml")
        html = remove(soup, tag)


    with open(filename, 'w') as fh:
        fh.write(soup.prettify())

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        main(arg)
