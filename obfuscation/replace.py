import re

#data = " 'Thid id'.replace('d','s') an example"

def formatReplace(data):
    rep = re.findall(r"\"\w+?\"\.replace\(\".\"\,\".\"\)", data, re.IGNORECASE)
    #print(rep[0])
    #["'Thid id'.replace('d','s')"]
    before = re.findall(r"\".+?\"\.", rep[0])[0]
    key = re.findall(r"\(\".\"\,\".\"\)",rep[0])
    #print(before)
    #print(key)
    #'Thid id'.
    #["('d','s')"]
    b = re.findall(r"[a-zA-Z]",key[0])
    after = before.replace(b[0], b[1])
    after = after.replace(".","")
    after = after.replace("'", "")

    data = data.replace(rep[0], after)
    #print(data)
    return(data)
    # This is an example
