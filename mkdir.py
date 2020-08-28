import os
import sys

def make_at(path, dirname):
    orig_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dirname)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(orig_path)

