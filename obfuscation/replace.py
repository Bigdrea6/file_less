import re


def format_replace(content_data):
    target = re.findall(r"\"\w+?\"\.replace\(\".\"\,\".\"\)", content_data, re.IGNORECASE)
    
    before = re.findall(r"\".+?\"\.", target[0])[0]
    key = re.findall(r"\(\".\"\,\".\"\)",target[0])
    
    b = re.findall(r"[a-zA-Z]",key[0])
    
    after = before.replace(b[0], b[1])
    after = after.replace(".", "")
    after = after.replace("'", "")

    after_replace = content_data.replace(target[0], after)

    return (after_replace)
