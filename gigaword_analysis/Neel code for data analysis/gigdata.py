import os
import json

count_file = 0
word_count = 0
word_dic = {}

# This is path of data folder
path = '/media/neel/Extra/gigaword_eng_5/data/afp_eng/'
# This is path of output file
outfile = open("/media/neel/Extra/gigaword_eng_5/total_count.json", "w")
outfile_word = open("/media/neel/Extra/gigaword_eng_5/word_freq_count.json", "w")

for filename in os.listdir(path):
    # File count
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
            # break
    file.close()
    # break
total_detail = {}
total_detail['total_file'] = count_file
total_detail['total_word'] = word_count

json.dump(total_detail, outfile)
outfile.close()

json.dump(word_dic,outfile_word)
outfile_word.close()
print(total_detail)
print(word_dic)
