import base64
import re


def base64_dec(content_data):
    target = re.findall(r"\[System.Convert\].+base64.+\)", content_data, re.IGNORECASE)
    
    target = re.findall(r"\".+\"", target[0])
    
    dec =  base64.b64decode(target[0][1:-1])
    dec = dec.decode()
    
    after_replace = re.sub(r"\[System.Convert\].+FromBase64String\(\".+\"\)", dec, content_data)
    
    return (after_replace)
