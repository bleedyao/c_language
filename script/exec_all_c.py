#!/usr/bin/env python3
import os

def exec():
    work_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(os.path.dirname(work_dir),'src')
    print(src_dir)
    for path,dir_list,file_list in os.walk(src_dir):
        for file in file_list:
            if os.path.splitext(file)[1] == '.c':
                compile(os.path.join(path,file))

def compile(file):
    os.system('gcc {}'.format(file))
    execOut(file)

def execOut(file):
    print(os.path.basename(file),'========>')
    os.system('./a.out')
    print()
if __name__=='__main__':
    exec()
