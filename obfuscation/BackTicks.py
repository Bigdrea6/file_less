#TODO:クラスに書き換える

import re

#data = 'th`nis`\
#i`s te`\
#st data.'



simbol = ["$", "&", "'", '"', "'" ]

result = []

def backticks(data):
    data_list = list(data)
    # print(data_list)
    for i in range(len(data_list)):
        #print(len(data_list))
        if data_list[i] == "`":
            if data_list[i+1] == "n":
                del data_list[i+1]
                data_list.append(" ")
                i += 1
            elif data_list[i+1] == "\\" and data_list[i+2] == "n":
                result.append(data_list[i])
            else:
                pass
        else:
            result.append(data_list[i])
    return(result)
