#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = list(s)
    final = ''
    if(65 <= ord(s[0]) <= 91):
        s[0]= s[0]
    else:
        s[0] = s[0].swapcase()
    
    for i in range(len(s)):
        if(s[i] == ' '):
            if(65 <= ord(s[i+1]) <= 91):
                s[i+1] = s[i+1]
            else:
                s[i+1]= s[i+1].swapcase()
        final = final + s[i]
    return(final)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
