import os, time, sys
from os import system as sm
from time import sleep as sp
from sys import platform as pf

sm('clear')
print("\033[1;32nCHECKING UPDATE")
sp(5)
sm("git pull")
sm('clear')
print("\033[1;32mUPDATE DONE")
print("\033[1;36mNow Run python excaa.py")
