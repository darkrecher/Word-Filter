# -*- coding: utf-8 -*-

"""
This will create a dist directory containing the executable file, and other
 stuff needed by that executable.

To launch it, run the command : 
python setup.py py2exe

Works with the following installations
py2exe-0.6.9.win32-py2.5.exe
python-2.5.4.msi

May work with newer versions, but it was not tested, because of the 
MSVCR90.dll crapness. 
See http://www.py2exe.org/index.cgi/Tutorial, chapter 5.
"""

from distutils.core import setup
import py2exe
    
setup(console=["main.py"])    
    
