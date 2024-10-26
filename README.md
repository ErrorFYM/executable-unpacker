# Executable unpacker

This project will be useful for people, who want to create **executable unpacker** for example for their friends to install.

Will be especially useful for people, who use linux and can create .tar.xz archive any moment, but friend uses windows.

## Dependencies

You need `python3` and `python3-venv` for this project to work.

#### On linux (Debain-like)

```shell
sudo apt install python3 python3-venv
```

#### On windows

Go to [Python website](https://www.python.org/) and download latest version for windows.
When downloaded open it and install in default directory. Also make sure to check **[X] Add to PATH**.

## Usage

First you need to move, copy or create symb-link in `archive` folder. Then in `config.py` change value of the variable `archive_name` to your archive name you put in `archive` folder. Like this:

```python
archive_name = "archive.tar.xz"  # must be tar format, any method could be used. symbolic links could be used
```

Also you could just rename your archive file, but the program name will be as your archive name (without extensions)

#### Linux

Then on linux you need to run `./build.sh` file, which will create venv using `create_venv.sh` file compile your app and archive in linux executable. If `./build.sh` won't run, because "Permission denied". Make yourself able to execute this file with command: 

```shell
chmod u+x ./build.sh ./create_venv.sh
```

`build` folder and `filename.spec` file will be also deleted if you use `./build.sh`. You can change that at will.

If `./build.sh` unable to create venv or it come out bugged you can create it yourself (with the same name)
To do that make sure you have `python3-venv` package installed:

```python
python3 -m venv venv_linux
```

Then you'll need to install pyinstaller to that venv so run:

```shell
./venv_linux/bin/python3 -m ensurepip
./venv_linux/bin/pip install pyinstaller
```

#### Windows

On Windows you'll need `python` installed.

Then run:

```shell
python -m ensurepip
pip install pyinstaller

pyinstaller -F --add-data archive/archive_name.tar.xz:archive -n your_app_name main.py
```

Replace `archive_name.tar.xz` with your archive name you entered in `config.py`
and `your_app_name` with your app name.

In `dist` folder you'll get your executable archive.



## To-do

- [ ]  Add `python3-rich` library usage (configurable)

- [ ]  Add custom icon support.

- [ ]  Make GUI **executable unpacker**

- [ ]  Make GUI **creator of executable unpacker**, that will work even without python installed

- [ ]  Add checksum checker for every single file in archive or just archive.
