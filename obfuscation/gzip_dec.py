import gzip, base64
import re


def gzip_dec(content_data):
    if re.search(r"New-Object.+gzip.+Decompress\)", content_data, re.IGNORECASE):
        target = re.findall(r"GzipStream\(.+Decompress\)", content_data, re.IGNORECASE)

        if re.search(r".+base64.+", content_data, re.IGNORECASE):
            target = re.findall(r"\".+\"", target[0])
            b64_dec = base64.b64decode(target[0][1:-1])
            gzip_dec = gzip.decompress(b64_dec)
            gzip_dec = gzip_dec.decode()

    after_replace = re.sub(r"New-Object IO.Compression.GzipStream\(.+Decompress\)", gzip_dec, content_data)

    return (after_replace)