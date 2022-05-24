import re


def format_plus(content_data):
    if (re.search(r"\+", content_data)):
        after_replace = re.sub(r"(\"\s|\"|\'|\'\s)\+(\s\"|\"|\'|\s\')", '', content_data)
    
    return (after_replace)
