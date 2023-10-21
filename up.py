import os, time, sys
from os import system as sm
from time import sleep as sp
from sys import platform as pf

sm('clear')
print("\033[1;32nCHECKING UPDATE")
sp(5)
if "Already up to date." in str(sm('git pull')):
    print("UPDATED")
else:
    print("New Version Found")
    sm('git pull')
