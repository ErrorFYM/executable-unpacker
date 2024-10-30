#! /usr/bin/bash

if [ ! -d "venv_linux" ]; then ./create_venv.sh
fi

./venv_linux/bin/pyinstaller -F --add-data "archive/$(./venv_linux/bin/python3 -c 'from config import archive_name; print(archive_name)')":archive -n "$(./venv_linux/bin/python3 -c 'from config import archive_name; print(archive_name.split(".tar")[0])')" main.py
rm -r build
rm "$(./venv_linux/bin/python3 -c "from config import archive_name; print(archive_name.split('.tar')[0])").spec"
