File descriptors are base structures in the Unix-like OS's. Before jumping in the networks it is important 

https://en.wikipedia.org/wiki/File_descriptor


https://stackoverflow.com/questions/5256599/what-are-file-descriptors-explained-in-simple-terms. Read most answers

** the /proc file system
https://www.tecmint.com/exploring-proc-file-system-in-linux/

The video below also speechs about /proc filesystem: https://www.youtube.com/watch?v=MHv6cWjvQjM

https://unix.stackexchange.com/questions/385771/writing-to-stdin-of-a-processma

CHALLENGE TIME!

This challenge considers you're using a compatible linux environment.

You should create a simple "echo" program that outputs the terminal standard input. 

Send information to your program not via terminal, instead, use its STDIN file descritor. You can use "echo"