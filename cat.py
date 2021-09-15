"""Implementing the cat shell command in python."""

import sys
#imports "sys" library using "import" keyword
from lib.helper import cat, readfile
#imports defined functions "cat", "readfile" from "lib.helper" using keywords "import" and "from"
TEXT = None
#initializes the value of  variable "TEXT" to None
ARG_CNT = len(sys.argv) - 1
# Using function "len", finds the length of the list, subtracts it by integer "1"
# save in a variable "ARG_CNT"
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
# if "ARG_CNT" equal to integer "0", read the standard input and save in "TEXT" variable
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
#if variable "ARG_CNT" equal to integer "1", save the 1st argument of the list as "filename"
#execute readfile function on the argument "filename" and save the output to variable "TEXT"
if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")
#if variable "ARG_CNT" is greater than integer "1" , print the name of the current python script followed by  "doesn't handle more than one arguement"
print(cat(TEXT))
#execute "cat" function on the argument "TEXT" and print the return from the function
