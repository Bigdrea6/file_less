import base64
import re

data = '[System.Convert]::FromBase64String("ZXhhbXBsZQ==")'

def base64_dec(content_data):
    if re.search(r"\[System.Convert\].+base64.+\)", content_data, re.IGNORECASE):
        enc_data = re.findall(r"\".+\"", content_data)
        return base64.b64decode(enc_data[0][1:-1])


dec_data = base64_dec(data)
print(dec_data.decode())
# example
