import io
import os
import sys

f = open("indian-name.txt")
ans_dic = {}
for name in f.readlines():
   ans_dic[str(name.strip())] = "None"
f.close()

with io.open("indian-name-2.txt",'w',encoding='utf-8') as f:
    for key in ans_dic:
        f.write(key+'\n')
f.close()
