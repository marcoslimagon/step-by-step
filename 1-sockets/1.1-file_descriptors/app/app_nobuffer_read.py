import sys
import select
import tty
import termios
from os import getpid




print(f'Hello world! Process: { getpid() }')

def isData(fd):
    return select.select([fd], [], [], 0) == ([fd], [], [])


with open(f'/proc/{sys.argv[1]}/fd/1', 'r') as fd:
    while 1:
        if isData(fd):
            c = fd.read(1)
            print(c, end="", flush=True)