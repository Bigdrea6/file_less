import re


def formatPlus(data):
    if (re.search(r"\+", data)):
        data = re.sub(r"(\"\s|\"|\'|\'\s)\+(\s\"|\"|\'|\s\')", '', data)
    
    return (data)
