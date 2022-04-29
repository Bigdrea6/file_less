import re


simbol = ["$", "&", "'", '"', "'" ]
result = []

def backticks(data):
    data_list = list(data)

    for i in range(len(data_list)):
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

    return (result)
