import sys
import tarfile
from os.path import abspath, expanduser
from os.path import isdir as path_isdir
from os.path import join as path_join

import config  # config.py

userdir = expanduser("~")
archive_path = path_join("./archive/", config.archive_name)

def get_resource_path(path):
    try:  # for executable(pyinstaller)
        return path_join(sys._MEIPASS, path)  # sys._MEIPASS is default pyinstaller executable path
    except:  # for python code
        return abspath(path)

config.set_messages()  # setting messages with up to date information

path = ""
if config.can_change_unpack_path:
    path = input(config.msg_path_input)
if path == "":
    path = config.default_unpack_path

config.unpack_path = abspath(expanduser(path))
config.set_messages()  # setting messages with up to date information

with tarfile.open(get_resource_path(archive_path), 'r') as file:
    print("\r" + config.msg_extracting_to, end="", flush=True)
    try:
        file.extractall(config.unpack_path)
    except NotADirectoryError:
        print("")  # new line
        print(config.msg_NotADirectoryError)
        sys.exit()
    print("\r" + config.msg_extracted_successfully
          + " " * (len(config.msg_extracting_to_pure) - len(config.msg_extracted_successfully_pure)))  # rewrite previus message with spaces
