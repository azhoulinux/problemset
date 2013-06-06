#!/usr/bin/env python
# encoding: utf-8
"""
update.py

Created by Darcy Liu on 2013-06-07.
Copyright (c) 2013 OnlineJudge. All rights reserved.
"""

import sys
import os
import codecs
import json
import jinja2

skip_files = ['.git','template','docs']
def main():
  with codecs.open('index.html', 'w', encoding='utf8') as outfile:
    problems = []
    for name in os.listdir('.'):
      if os.path.isdir(name) and name not in skip_files:
        path = os.path.join('.',name,'problem.json')
        problem = codecs.open(path, encoding='utf8').read()
        problem = json.loads(problem)
        print problem['id'],problem['title']
        problems.append(problem)
    template = jinja2.Template(open('base.html').read())
    outfile.write(template.render(locals()))


if __name__ == '__main__':
  main()

