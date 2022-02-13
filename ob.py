import numpy as np

'''
Unicodeの0x21(!)から0x7E(~)に対応する文字の個数
character_listに格納する.
例えばcharacter_list[65]なら"A"の文字数が格納されている
(AのUnicodeポイントは0x41 = 65)
'''
C = 96 
character_list = np.zeros(C)
number = 0

'''
file.txtは入力のつもり
ログファイルとどう相関させるかは考えていない
'''
f = open('file.txt', 'r')
line = f.readline()


'''
ファイルから一行ずつ読み込んで,
ファイル内の文字とその個数を配列に格納する
'''
while line:
    #print(line)
    for s in line:
        code_point = ord(s) #  コードポイントを得る
        #print(s.isupper())
        #print(s)
        #print(code_point)
        key = code_point - 32 #  コードポイントの値を配列のインデックスに合わせる
        #print(key)
        if  0 <= key <= 96 : #  配列のインデックス外の文字は無視する
            character_list[key] += 1 #  コードポイントに該当するインデックスをインクリメント
        number += 1 #  全体の文字数をカウント
    line = f.readline() #  次の行を読み込む


'''
インデックスだけで降順にソート
例えば [10, 13, 15, 17, 14, 12, 11] という配列があったら
[1, 2, 3, 4, 5, 6, 7]とインデックスだけ抽出し,
[4, 3, 5, 2, 6, 7, 1]と降順にソートする
実際の配列は並び変えたくなくて,どの要素が何番目に大きいかだけを知りたいため
'''
sorted_array = np.argsort(character_list)[::-1] 


'''
文字とその割合を計算している
'''
for tag in range(5): #  上位5位までを計算
    tmp = sorted_array[tag] #  [tag]番目に大きい配列のインデックスを[tmp]に入れる
    quantity = character_list[tmp] #  [tmp]の要素の値をquantityに入れる(これが文字の個数になる)
    tmp += 32 #  コードポイントをもとに戻す
    chara = chr(tmp) #  tmpはコードポイントでもあったので,対応する文字をcharaに入れる
    ratio = quantity / number #  該当文字の全体の割合を出す
    #print(ratio)
    #print(tmp)
    #print(chara)
    print(chara + ' : ' + str(ratio * 100) + '%') #  結果を出力する

#print (sorted_array)
#for i in range(C):
#    print(str(character_list[i]) + ' ' + str(i))
f.close()
