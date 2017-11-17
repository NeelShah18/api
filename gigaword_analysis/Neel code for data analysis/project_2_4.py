# This code gives back JSON file for:
# -->  only in the documents where this word appears: what is the average frequency of the word in the documents(number of time the word appears divided by number of words in the document)

import os
import json

count_file = 0
word_count = 0
word_dic = {}
result_dic = {}
# This is path of data folder
path = '/media/neel/Extra/gigaword_eng_5/data/afp_eng/'
# This is path of output file

for filename in os.listdir(path):
    # File count
    file_add = ("/media/neel/Extra/gigaword_eng_5/freq_ans/{}.json".format(str(filename)))
    outfile = open(file_add, "w")
    count_file += 1
    file = open(path+filename,"r")
    text = file.read().lower()
    # Fetching only <p> </p> tage data
    for item in text.split("</p>"):
        if "<p>" in item:
            temp_lis = []
            data = str(item [ item.find("<p>")+len("<p>") : ])
            data = data.replace(',','').replace('.','').replace('"','').replace("'","").replace("(","").replace(")","").replace('\n',' ').replace("-","")
            temp_lis = data.split(" ")
            # counting words
            for word in temp_lis:
                word_count += 1
                try:
                    word_dic[str(word)] = int(word_dic[str(word)]) + 1
                except:
                    word_dic[str(word)] = 1

    for key in word_dic:
        val = int(word_dic[key])/word_count
        result_dic[key] = float(format(val*100000,'.2f'))
    file.close()
    json.dump(result_dic, outfile)
    outfile.close()

print('done')
