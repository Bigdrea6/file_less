import re
import numpy as np
import commentout

'''
Unicodeの0x21(!)から0x7E(~)に対応する文字の個数
character_listに格納する.
例えばcharacter_list[65]なら"A"の文字数が格納されている
(AのUnicodeポイントは0x41 = 65)
'''
com = commentout.comment('file.txt')
com.comment()
C = 96 
character_list = np.zeros(C)
number = 0
m_brackets = 0
sbra = 0
cbra = 0
repl = 0
flag = 0

swap = r'\{\d+\}' #{数字}を探索
rchar = r'\[char\]'
rep = r'\-replace'
reswap = re.compile(swap)
rechar = re.compile(rchar)

'''
file.txtは入力のつもり
ログファイルとどう相関させるかは考えていない
'''
f = open('Obfu.txt', 'r')
line = f.readline()


'''
ファイルから一行ずつ読み込んで,
ファイル内の文字とその個数を配列に格納する
'''
while line:
    m_brackets = len(re.findall(swap, line))
    b_brackets = len(re.findall(rchar, line))
    replace = len(re.findall(rep, line))
    for s in line:
        code_point = ord(s) #  コードポイントを得る
        key = code_point - 32 #  コードポイントの値を配列のインデックスに合わせる
        if  0 <= key <= 96 : #  配列のインデックス外の文字は無視する
            character_list[key] += 1 #  コードポイントに該当するインデックスをインクリメント
        number += 1 #  全体の文字数をカウント
    sbra += m_brackets
    cbra += b_brackets
    repl += replace
    if (line[len(line)-2] + line[len(line)-1]) == '==': #==の検知
        flag = 1
    line = f.readline() #  次の行を読み込む



'''
各難読化
'''
print('--Obfuscation detection---------------------')
print('      Obfuscation      |quantity|  ratio')
quantity = character_list[7]
if (quantity >= 1):
    ratio = quantity / number
    print('  \'(backtick)        ' + '  |  ' + str(quantity) + '  |  ' + str(ratio * 100) + '%')
    flag = 1

quantity = cbra
if (quantity >= 1):
    ratio = quantity / number
    print('  [](square brackets)' + '  |  ' + str(quantity) + '  |  ' + str(ratio * 100) + '%')
    flag = 1

quantity = sbra
if (quantity >= 2):
    ratio = quantity / number
    print('  {}(curly brackets) ' +  '  |  ' + str(quantity) + '  |  ' + str(ratio * 100) + '%')
    flag = 1

quantity = character_list[6]
if (quantity >= 1):
    ratio = quantity / number
    print('  &(Ampersand)       ' +  '  |  ' + str(quantity) + '  |  ' + str(ratio * 100) + '%')
    flag = 1



quantity = repl
if (quantity >= 1):
    ratio = quantity / number
    print('   -replace(hyphen)  ' +  '  |  ' + str(quantity) + '  |  ' + str(ratio * 100) + '%')
    flag = 1

if (flag == 1):
    print('The above obfuscation has been detected.')

print('\n')

'''
各文字の分散
'''
upper = 0
lower = 0
number = 0

print('--Characters Ratio------------')
for num in range(26):
    quantity = character_list[num + 33]
    upper += quantity

for num in range(26):
    quantity = character_list[num + 65]
    lower += quantity

for num in range(10):
    quantity = character_list[num + 16]
    number += quantity

characters = upper + lower
sum = characters + number

print('The ratio of the numbers is ' + str((number * 100) // sum) +'%')
if (number / sum) > 0.1 :
    print('It seems to have been obfuscated.')
    print('The ratio of the numbers is ' + str((number * 100) // sum) +'%')
    flag = 1

print('The ratio of the upper is ' + str((upper * 100) // characters) +'%')
if (upper / characters) > 0.3 :
    print('It seems to have been obfuscated.')
    print('The ratio of the upper is ' + str((upper * 100) // characters) +'%')
    flag = 1

if (flag == 0) :
    print('No obfucation was detected.')

if (flag == 1) :
    print('Obfucation was detected.')
   

f.close()
