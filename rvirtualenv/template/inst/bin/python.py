#!/usr/bin/env python

'''
use this file directly, or just set PYTHONPATH to your virtualenv directory
and run system wide python instance
'''

import os, sys
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

def win_quote_argv(argv):
    '''
    Windows platform needs add quotes around arguments with spaces
    '''
    def q(arg):
        if ' ' in arg:
            return '"%s"' % arg
        else:
            return arg
    return map(q, argv)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if sys.platform == 'win32':
        argv = win_quote_argv(argv)
    inject_pythonpath()
    os.execvp(sys.executable, argv)

if __name__ == '__main__':
    main()

