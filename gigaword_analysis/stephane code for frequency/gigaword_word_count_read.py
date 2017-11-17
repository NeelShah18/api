import json

gigaword_folder = "/Users/stephane/DatalogProjects/data/gigaword_eng_5"

infile = open(gigaword_folder + "/word_count.json", "r")
word_counts = json.load(infile)