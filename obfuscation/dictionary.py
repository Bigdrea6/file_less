import re
import ascii
import Back_Ticks as back
import base64_decode as base 
import plus_division as plus
import Reorder as reorder
import replace
import gzip_dec as gzip

data = '[char]84+his ("{1}{0}" -f"s","i") an "dxampld".replace("d","e") [System.Convert]::FromBase64String("ZXhhbXBsZQ==")'

def check(data):
    if re.search(r".*'gzip'.*", data, re.IGNORECASE):
        data = gzip.gzip_dec(data)
    if re.search(r"\[System.Convert\].+base64.+\)", data, re.IGNORECASE):
        # print("base")
        data = base.base64_dec(data)
        #print(data)
    if re.search(r".*\[char\].*", data, re.IGNORECASE):
        #print("char")
        data = ascii.formatAscii(data)
        #print(data)
    if re.search(r".*\.replace.*", data, re.IGNORECASE):
        data = replace.formatReplace(data)
        #print(data)
    if re.search(r"\"(\{\d\})+\"", data, re.IGNORECASE):
        #print("order")
        data = reorder.formatReorder(data)
        #print(data)
    if re.search(r"\'\+\'", data, re.IGNORECASE):
        data = plus.formatPlus(data)
        print(data)
    if re.search(r"\'\+\'", data, re.IGNORECASE):
        data = back.backticks(data)
    print(data)

check(data)
