import base64
import re

data = '[System.Convert]::FromBase64String("ZXhhbXBsZQ==")'

def base64_dec(content_data):
    enc_data = re.findall(r"\[System.Convert\].+base64.+\)", content_data, re.IGNORECASE)
    #print(enc_data[0])
    enc_data = re.findall(r"\".+\"", enc_data[0])
    #print(enc_data[0])
    result =  base64.b64decode(enc_data[0][1:-1])
    result = result.decode()
    #print(type(result))
    #print(result)
    after_replace = re.sub(r"\[System.Convert\].+FromBase64String\(\".+\"\)", result, content_data)
    return(after_replace)
