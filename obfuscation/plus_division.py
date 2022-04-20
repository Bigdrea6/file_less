import re

#data = " 'this is an exa' + 'mple 5 + 2' "

def formatPlus(data):
    if(re.search(r"\+", data)):
        data = re.sub(r"(\"\s|\"|\'|\'\s)\+(\s\"|\"|\'|\s\')", '',data)
    return(data)
    # 'this is an example 5 + 2'
