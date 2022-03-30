import re

data = "[char]84+hi+[char]115+ [char]105+s an example+[char]33"

def formatAscii(data):
    #numbox = []
    #i = 0
    asciis = re.findall(r'\+*\[char\](0x)*\d+\s*\+*', data)
    print(asciis)
    # ['char[84]', 'char[115]', 'char[105]', 'char[33]']

    for c in asciis:
        num = re.search(r'\d+', c)
        #numbox.append(int(num.group()))
        #i += 1
        #m = re.compile(c)
        chrs = chr(int(num.group()))
        print(chrs)
        # T\n s\n i\n !

        data = data.replace(c, chrs)
    
    print(data)
    # This is an example!


formatAscii(data)
