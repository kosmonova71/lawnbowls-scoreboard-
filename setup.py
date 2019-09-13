import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('Scoreboard.py', base=base)
]

setup(name='Scoreboard',
      version='0.1',
      description='Lawn Bowls Scoreboard',
      executables=executables
      )
