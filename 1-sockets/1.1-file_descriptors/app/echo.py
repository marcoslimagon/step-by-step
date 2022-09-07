import sys
from os import getpid

print(f'Hello world! Process: { getpid() }')


for line in sys.stdin:
    print(f'Echoing: {line}')
