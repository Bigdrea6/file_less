import re


def formatAscii(data):
    asciis = re.findall(r'\+*\[char\]\d+\s*\+*', data)

    for c in asciis:
        num = re.search(r'\d+', c)
        chrs = chr(int(num.group()))
        data = data.replace(c, chrs)
    
    return (data)
