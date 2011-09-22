#!/usr/bin/python2.7

'''
use this file directly, or just set PYTHONPATH to your virtualenv directory
and run system wide python instance
'''

import os, sys, runpy
from os.path import join, dirname, pardir, abspath


def get_this_path():
    '''
    we do expect scripts are installed just one level deeper from venv
    '''
    return abspath(dirname(dirname(__file__)))

def inject_pythonpath():
    '''
    insert virtualevn path into pythonpath
    '''
    pypath = os.environ.get('PYTHONPATH', '').split(os.path.pathsep)
    thispath = get_this_path()
    for path_to_remove in ('', thispath):
        try:
            pypath.remove(path_to_remove)
        except ValueError:
            pass
    pypath.insert(0, thispath)
    os.environ['PYTHONPATH'] = os.path.pathsep.join(pypath)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    inject_pythonpath()
    os.execvp(sys.executable, argv)

if __name__ == '__main__':
    main()

