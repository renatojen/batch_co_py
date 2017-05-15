import glob
from os import rename, path, makedirs
from shutil import copy2

i = 0
prefix = "OP"
suffix = ""
if not path.exists('./new/'):
    makedirs('./new/')
for filename in glob.iglob('./level1/**/*.jpg', recursive=True):
    i = i + 1
    print(str('{:06}'.format(i)) + ' - ' + filename + ' - ' + path.basename(filename) + ' - ' + path.dirname(path.realpath(filename)))
    copy2(filename, './new/' + prefix + str('{:06}'.format(i)) + suffix +  ".jpg")