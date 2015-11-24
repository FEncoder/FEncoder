#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
remove outdated file or directory
- file/dir

remove outdated directory tree
--dir

create new directory
+ dir

copy new file or directory
++src|dst

copy existed file or directory
c src|dst

move existed file or directory
m src|dst

rename existed file or directory
r src|dst
"""


import os
import sys
import shutil

# exceptions!!!

class DirectoryNotFoundError(Exception):
    pass


dst_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
# random!!!
src_dir = os.path.join(os.environ['TEMP'], 'FEncoder')

# make dir!!!

# downloading!!!

# vdf

with open(os.path.join(src_dir, 'R2.vdf'), 'rb') as f:
    for line in f:
        line = line.decode().strip()
        content = line[2:]
        if line[0:2] == '- ':
            if os.path.isdir(content):
                os.rmdir(content)
            elif os.path.isfile(content):
                os.remove(content)
        elif line[0:2] == '--':
            shutil.rmtree(content)
        elif line[0:2] == '+ ':
            os.mkdir(content)
        elif line[0:2] == '++':
            src_path, dst_path = content.split('|')
            src_path = os.path.join(src_dir, src_path)
            dst_path = os.path.join(dst_dir, dst_path)
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dst_path)
        elif line[0:2] == 'c ':
            src_path, dst_path = content.split('|')
            src_path = os.path.join(dst_dir, src_path)
            dst_path = os.path.join(dst_dir, dst_path)
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dst_path)
        elif line[0:2] == 'm ':
            src_path, dst_path = content.split('|')
            src_path = os.path.join(dst_dir, src_path)
            dst_path = os.path.join(dst_dir, dst_path)
            shutil.move(src_path, dst_path)
        elif line[0:2] == 'r ':
            src_path, dst_path = content.split('|')
            src_path = os.path.join(dst_dir, src_path)
            dst_path = os.path.join(dst_dir, dst_path)
            os.rename(src_path, dst_path)

