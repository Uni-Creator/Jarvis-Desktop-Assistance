import re

def match(input,sample):
    for i in input:
        if re.search(i,sample):
            return True
    return False
