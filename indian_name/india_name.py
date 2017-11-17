import sqlite3
import sys
import os
import io

def cleanName(m_name):
    lis = []
    lis = m_name
    result_lis = {}
    for data in lis:
        text = str(data)
        text = (((((text[2:len(text)-3].rstrip()).replace("@","")).replace("smt.","")).strip()).replace(".","")).replace("smt","")
        temp_lis = text.split(" ")
        if len(temp_lis[0]) > 2:
            #print(temp_lis[0])
            result_lis[str(temp_lis[0])] = 0
    return result_lis

def writeIt(name_dic):
    w_lis = []
    for key in name_dic:
    w_lis = name_dic
    filename = '/home/neel/indian-name.txt'
    with io.open(filename,'a',encoding='utf-8') as f:
        for data in w_lis:
            f.write(data+'\n')
    return None

def main():
    sqlite_database = '/home/neel/indian_name.sqlite'
    conn = sqlite3.connect(sqlite_database)
    c = conn.cursor()
    m_name = []
    c.execute("SELECT `name` FROM `Indian-Female-Names`;")
    m_name = c.fetchall()
    name_dic = cleanName(m_name)
    result = writeIt(name_dic)
    print('done!')

if __name__=='__main__':
    main()
