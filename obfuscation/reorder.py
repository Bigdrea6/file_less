import re


def format_reorder(content_data):
    if (re.search(r"-f", content_data, re.IGNORECASE)):
        target = re.findall(r"\"(\{.*\})\"", content_data, re.IGNORECASE)
        target = re.findall(r"\{\d\}", target[0])
        brackets = "\{\}"

        for i in range(len(target)):
            for x in range(len(brackets)):
                target[i] = target[i].replace(brackets[x],'')

        target1 = re.findall(r"-f\".*\)", content_data, re.IGNORECASE)
        target1 = re.findall(r"\".*?\"", target1[0])
        exchanged = list()

        for entry in target:
            exchanged.append(target1[int(entry)])

        exchanged = ''.join(exchanged).replace('\"','')
        after_replace = re.sub(r"\(\"(\{\d\})+?\"\s-f\"\w\"(,\"\w\")*\)", exchanged, content_data)
        
        return (after_replace)
