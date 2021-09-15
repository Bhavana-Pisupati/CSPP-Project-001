"""Implementing the wc shell command in python."""

import sys
#imports "sys" library using "import" keyword
from lib.helper import wc, readfile
#imports defined functions "head", "readfile" from "lib.helper" using keywords "import" and "from"
TEXT = None
#initializes the value of variable "TEXT" to None
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
response = wc(TEXT)
#execute "wc" function on the argument "TEXT" and save the return from the function to "response"
print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))
# Read each argument of "response" as a string and print them separated by spaces