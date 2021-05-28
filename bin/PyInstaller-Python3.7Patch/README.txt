Date: 2019 - 06 - 01

Description: 
- There's a bug re: Python 3.7 & PyInstaller when PyInstaller is installed
to a projects virtual environment. 

- Without a patch to this, attempting to compile a program to exe with 
PyInstaller will fail with the following error returned by PyInstaller: 
TypeError: Expected str, bytes or os.PathLike object, not NoneType

- This is a common problem, and thankfully someone has posted a fix to this on github

- By replacing the binddepend.py within your projects PyInstaller directory installed to the
virtual environment; e.g., \bin\env\Lib\site-packages\PyInstaller\depend with the file in this directory,
running PyInstaller to compile your program to exe should work

- Only do this after installing PyInstaller to your project's virtual environment

- Source of recommendation for this fix: https://stackoverflow.com/questions/54138898/an-error-for-generating-an-exe-file-using-pyinstaller-typeerror-expected-str
- Source of fix: https://github.com/Loran425/pyinstaller/commit/14b6e65642e4b07a4358bab278019a48dedf7460