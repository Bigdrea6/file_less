import re
from winreg import REG_FULL_RESOURCE_DESCRIPTOR
import ascii
import Back_Ticks as back
import base64_decode as base 
import plus_division as plus
import Reorder as reorder
import replace
import gzip_dec as gzip


data = '[char]84+his ("{1}{0}" -f"s","i") an "dxampld".replace("d","e") [System.Convert]::FromBase64String("ZXhhbXBsZQ==")'
#data = '[System.Convert]::FromBase64String("ZXhhbXBsZQ==")'

re_gzip = re.compile(r".*'gzip'.*",re.IGNORECASE)
re_base64 = re.compile(r".*\[System.Convert\].+base64.+\).*",re.IGNORECASE)
re_ascii = re.compile(r".*\[char\].*",re.IGNORECASE)
re_replace = re.compile(r".*\.replace.*",re.IGNORECASE)
re_order = re.compile(r".*\"(\{\d\})+\".*",re.IGNORECASE)
re_plus = re.compile(r".*\'\+\'.*",re.IGNORECASE)
re_backticks = re.compile(r".*\`.*",re.IGNORECASE)


dec_array = [re_gzip, re_base64, re_ascii, re_replace, re_order, re_plus, re_backticks]
dec_func = {0:gzip.gzip_dec, 1:base.base64_dec, 2:ascii.formatAscii, 3:replace.formatReplace, 4:reorder.formatReorder, 5:plus.formatPlus, 6:back.backticks}


def check(data):
    while(True): # 変更が一回もなければ完了したとみなす
        changed = 0
        for i in range(len(dec_array)):
            if dec_array[i].match(data):
                #print(dec_array[i])
                data = dec_func[i](data)
                changed = 1
                #print(data)
        if changed == 0:
            break
        print(data)

check(data)
