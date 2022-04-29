import re


def formatreplace(data):
    rep = re.findall(r"\"\w+?\"\.replace\(\".\"\,\".\"\)", data, re.IGNORECASE)
    
    before = re.findall(r"\".+?\"\.", rep[0])[0]
    key = re.findall(r"\(\".\"\,\".\"\)",rep[0])
    
    b = re.findall(r"[a-zA-Z]",key[0])
    
    after = before.replace(b[0], b[1])
    after = after.replace(".", "")
    after = after.replace("'", "")

    data = data.replace(rep[0], after)

    return (data)
