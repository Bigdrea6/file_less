import re

#data = '$searcher = (New-Object System.Management.ManagementObjectSearcher((Binary2String(",.,.,,..,..,,.,.,..,..,,,..,,.,.,..,,,..,...,.,,,,.,,,,,,,.,.,.,,,.,,,,,,..,,..,,...,,.,,..,....,..,..,.,,.,,,,,,.,.,...,..,.,,.,..,...,,,..,,..,,..,,.,,.,.....,.,,,,..,..,....,..,..,.,...,,,,,...,.,.,...,.,,,..,,.,.,...,,.,,.,.,,..,....,,.,...,,..,...,.,,,..,,.,.,..,..,.".Replace(",", "0").Replace(".", "1")))))'

def formatReplace(data):
    rep = re.findall(r"\".+?\"\.Replace\(.+?\)", data, re.IGNORECASE)
    before = re.findall(r"\".+?\"\.", rep[0])[0]
    key = re.findall(r"\(.+?\)",rep[0])
    b = re.findall(r"\".\"",key[0])
    for i in range(len(b)):
        b[i] = b[i].replace('"', '')
    after = before.replace(b[0], b[1])

    data = data.replace(rep[0], after)
    return(data)
