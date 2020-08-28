import os
import glob


filesizes = { os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py') }
from pprint import pprint as pp
pp(filesizes)