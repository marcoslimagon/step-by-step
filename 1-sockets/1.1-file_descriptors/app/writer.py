from fcntl import ioctl
from termios import TIOCSTI
import sys


with open(f'/proc/{sys.argv[1]}/fd/0', 'w') as fd:
    for char in f'{sys.argv[2]}\n':
        ioctl(fd, TIOCSTI, char)