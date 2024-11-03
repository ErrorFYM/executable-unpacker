from os.path import expanduser

archive_name = "archive.tar.xz"  # must be tar format, any method could be used. symbolic links could be used

default_unpack_path = expanduser("~")  # user folder
can_change_unpack_path = True  # will client be able to change installation path in compilated file (if False, it will instantly extract all the files in default_unpack_path)

colored_terminal = True
restart_colors = "\x1b[0m"  # do not change

unpack_path = default_unpack_path

# Messages
def set_messages():  # setting messages with up to date information (will be called in main.py when ready)
    global msg_path_input, msg_extracting_to, msg_extracted_successfully
    msg_path_input = f"Enter target path(leave empty for {default_unpack_path} ): "

    global msg_extracting_to_pure, msg_extracting_to_color
    msg_extracting_to_pure = f"Extracting to {unpack_path}…"
    msg_extracting_to_color = "\x1b[1;33;43m"

    global msg_extracted_successfully_pure, msg_extracted_successfully_color
    msg_extracted_successfully_pure = "Successfully extracted."
    msg_extracted_successfully_color = "\x1b[0;32;40m"

    global msg_NotADirectoryError, msg_NotADirectoryError_pure, msg_NotADirectoryError_color
    msg_NotADirectoryError_pure = f"Error! File with name of the folder in archive already exists! Rename the file in {unpack_path} that could cause the issue!"
    msg_NotADirectoryError_color = "\x1b[0;31;40m"


    if colored_terminal:
        msg_extracting_to = msg_extracting_to_color + msg_extracting_to_pure + restart_colors
        msg_extracted_successfully = msg_extracted_successfully_color + msg_extracted_successfully_pure + restart_colors
        msg_NotADirectoryError = msg_NotADirectoryError_color + msg_NotADirectoryError_pure + restart_colors
    else:
        msg_extracting_to = msg_extracting_to_pure
        msg_extracted_successfully = msg_extracted_successfully_pure
        msg_NotADirectoryError = msg_NotADirectoryError_pure


