import gzip, base64
import re

data = 'New-Object IO.Compression.GzipStream([IO.MemoryStream][Convert]::FromBase64String("H4sIAKacLWIC/0utSMwtyEkFAJ+b7G4HAAAA"), [IO.Compression.CompressionMode]::Decompress)'

def gzip_dec(content_data):
    if re.search(r".+gzip.+", content_data, re.IGNORECASE):
        if re.search(r".+base64.+", content_data, re.IGNORECASE):
            enc_data = re.findall(r"\".+\"", content_data)
            b64_dec = base64.b64decode(enc_data[0][1:-1])
            return gzip.decompress(b64_dec)
        
        else:
            compress_data = re.findall(r"\(.+\,", content_data)
            return gzip.decompress(compress_data[0][1:-1])

dec_data = gzip_dec(data)
print(dec_data)
# example