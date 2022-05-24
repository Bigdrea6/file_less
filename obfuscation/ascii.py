import re


def format_ascii(content_data):
    target = re.findall(r'\+*\[char\]\d+\s*\+*', content_data)

    for c in target:
        num = re.search(r'\d+', c)
        chrs = chr(int(num.group()))
        after_replace = after_replace.replace(c, chrs)
    
    return (after_replace)
