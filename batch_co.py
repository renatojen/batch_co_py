import glob
from os import rename, path, makedirs
from shutil import copy2

prefix = "OP"
suffix = ""
if not path.exists('./new/'):
    makedirs('./new/')
for i, filename in enumerate(glob.iglob('./level1/**/*.jpg', recursive=True)):
    print(str('{:06}'.format(i)) + ' - ' + filename + ' - ' + path.basename(filename) + ' - ' + path.dirname(path.realpath(filename)))
    copy2(filename, './new/' + prefix + str('{:06}'.format(i)) + suffix +  ".jpg")
