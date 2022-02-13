import sys

args = sys.argv
f_name = args[1]

with open(f_name) as f:
    source = [s.strip() for s in f.readlines() if len(s.strip()) != 0]

check = []

for i in range(len(source)):
    if '#' == source[i][0] and '#>' not in source[i]:
        check.append(i)

for i in range(len(check)):
    source.pop(check[i]-i)

check.clear()

for i in range(len(source)):
    if  '<#' in source[i] or '#>' in source[i]:
        check.append(i)

diff = 0
for i in range(0,len(check),2):
    del source[check[i]-diff:check[i+1]-diff+1]
    diff += (check[i+1]-check[i]+1)

source = ''.join(source)
