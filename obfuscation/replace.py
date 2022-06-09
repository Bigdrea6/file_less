import re

# content_data = '$searcher = (New-Object System.Management.ManagementObjectSearcher((Binary2String(",.,.,,..,..,,.,.,..,..,,,..,,.,.,..,,,..,...,.,,,,.,,,,,,,.,.,.,,,.,,,,,,..,,..,,...,,.,,..,....,..,..,.,,.,,,,,,.,.,...,..,.,,.,..,...,,,..,,..,,..,,.,,.,.....,.,,,,..,..,....,..,..,.,...,,,,,...,.,.,...,.,,,..,,.,.,...,,.,,.,.,,..,....,,.,...,,..,...,.,,,..,,.,.,..,..,.".Replace(",", "0").Replace(".", "1")))))'

def format_replace(content_data):
    target = re.findall(r"\".+?\"\.Replace\(.+?\)", content_data, re.IGNORECASE)
    
    before = re.findall(r"\".+?\"\.", target[0])[0]
    key = re.findall(r"\(.+?\)",target[0])
    
    b = re.findall(r"\".\"",key[0])
    
    for i in range(len(b)):
        b[i] = b[i].replace('"', '')
    
    after = before.replace(b[0], b[1])

    after_replace = content_data.replace(target[0], after)
    
    print(after_replace)
    # return (after_replace)

# format_replace(content_data)