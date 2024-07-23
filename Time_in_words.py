import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here

    time = ['', 'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine']
    
    if m == 0:
        return time[h] + " o' clock"
    elif m == 30:
        return "half past " + time[h]
    elif m < 30:
        if m == 15:
            return "quarter past " + time[h]
        elif m == 1:
            return time[m] + " minute past " + time[h]
        else:
            return time[m] + " minutes past " + time[h]
    else:
        m = 60-m
        h += 1

        if m == 15:
            return "quarter to " + time[h]
        elif m == 1:
            return time[m] + " minute to " + time[h]
        else:
            return time[m] + " minutes to " + time[h]
h = int(input().strip())

m = int(input().strip())

result = timeInWords(h, m)

print(result)
