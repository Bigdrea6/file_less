import re


def formatReorder(contentdata):
    if (re.search(r"-f", contentdata, re.IGNORECASE)):
        exchange_index = re.findall(r"\"(\{.*\})\"", contentdata, re.IGNORECASE)
        exchange_index = re.findall(r"\{\d\}", exchange_index[0])
        brackets = "\{\}"

        for i in range(len(exchange_index)):
            for x in range(len(brackets)):
                exchange_index[i] = exchange_index[i].replace(brackets[x],'')

        exchange_sentence = re.findall(r"-f\".*\)", contentdata, re.IGNORECASE)
        exchange_components = re.findall(r"\".*?\"", exchange_sentence[0])
        exchanged = list()

        for entry in exchange_index:
            exchanged.append(exchange_components[int(entry)])

        exchanged = ''.join(exchanged).replace('\"','')
        raw_content = re.sub(r"\(\"(\{\d\})+?\"\s-f\"\w\"(,\"\w\")*\)", exchanged, contentdata)
        
        return (raw_content)
