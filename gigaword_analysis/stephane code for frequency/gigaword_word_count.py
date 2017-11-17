# create word count for english words in 2 hours
# gigaword.txt compiled by bash file

import re
import json
import string

gigaword_folder = "/Users/stephane/DatalogProjects/data/gigaword_eng_5"
infile = open(gigaword_folder + "/gigaword.txt", "r")
outfile = open(gigaword_folder + "/word_count_test.json", "w")

counter_doc = 0
counter_file_backup = 0
word_counts = {}
inline = infile.readline().lower()


chars_for_split = "[" + string.punctuation.replace("'", "") + " \n]"

while inline != '':# and counter_doc < 100005:  # end of the file == ''
    counter_doc += 1
    if counter_doc % 100000 == 1:
        print counter_doc, "out of 12,000,000"
        counter_file_backup += 1
        json.dump(word_counts,
                  fp=open(gigaword_folder + "/word_count" + str(counter_file_backup) + ".json",
                          "w"))
    counter = 0
    while counter < 5 and inline != '':
        while inline.strip() != '<text>' and inline.strip() != '':
            inline = infile.readline().lower()
        inline = infile.readline().lower()
        while inline.strip() != '</text>' and inline.strip() != '':
            if inline.strip() != '<p>' and inline.strip() != '</p>':
                words = re.split(chars_for_split, inline)
                # print words
                for w in words:
                    if w != '' and not w.isdigit():
                        if w in word_counts:
                            word_counts[w] += 1
                        else:
                            word_counts[w] = 1

                inline = infile.readline().lower()
                counter += 1
            else:
                inline = infile.readline().lower()

    inline = infile.readline().lower()

json.dump(word_counts, outfile)
outfile.close()

#
# for w in (word_counts.keys()):
#     print w, word_counts[w]
#
# import json
# dic = json.load(fp=open("/Users/stephane/DatalogProjects/data/gigaword_eng_5/word_count117.json", "r"))
# sum = 0
# max = 0
# for w in dic:
#     sum += dic[w]
#     if dic[w]>max:
#         max= dic[w]
#         wmax=w
# print sum, wmax, max
