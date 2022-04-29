import gzip, base64
import re

def gzip_dec(content_data):
    if re.search(r"New-Object.+gzip.+Decompress\)", content_data, re.IGNORECASE):
        enc_data = re.findall(r"GzipStream\(.+Decompress\)", content_data, re.IGNORECASE)

        if re.search(r".+base64.+", content_data, re.IGNORECASE):
            enc_data = re.findall(r"\".+\"", enc_data[0])
            b64_dec = base64.b64decode(enc_data[0][1:-1])
            result = gzip.decompress(b64_dec)
            result = result.decode()

    after_replace = re.sub(r"New-Object IO.Compression.GzipStream\(.+Decompress\)", result.decode(), content_data)

    return (after_replace)