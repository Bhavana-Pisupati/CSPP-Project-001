"""The python code helps to read the command line input for curl method."""

import sys
#imports "sys" library
from lib.helper import curl
#imports defined function "curl" from "lib.helper" using keywords "import" and "from"
URL = None
#initializes the value of variable "URL" to None
ARG_CNT = len(sys.argv) - 1
# Using function "len", finds the length of the list, subtracts it by integer "1"
# save in a variable "ARG_CNT"
if ARG_CNT != 1:
    print('Usage: curl [URL]...')
# if "ARG_CNT" is not equal to integer "1", print "Usage: curl [URL]..."
if ARG_CNT == 1:
    URL = sys.argv[1]
    #if variable "ARG_CNT" equal to integer "1", save the 1st argument of the list as "URL"
    if 'http' not in URL[:5]:
        URL = "http://"+URL
    # if http is not found in the url then add "http://" to the URL
    print(curl(URL))
#execute "curl" function on the argument "URL" and print the return from the function