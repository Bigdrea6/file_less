import re

data = '[char]84+his ("{1}{0}" -f"s","i") an dxampld.replace("d","e") [System.Convert]::FromBase64String("ZXhhbXBsZQ==")'

def check(data):
    if re.search(r".*base64.*", data, re.IGNORECASE):
        print("base64")
    if re.search(r".*gzip.*", data, re.IGNORECASE):
        print("gzip")
    if re.search(r".*\[char\].*", data, re.IGNORECASE):
        print("ascii")
    if re.search(r".*\.replace.*", data, re.IGNORECASE):
        print("replace")
    if re.search(r"\'\+\'", data, re.IGNORECASE):
        print("plus")

check(data)
