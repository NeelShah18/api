import sys
import codecs
import logging
import numpy as np
from UNICODE_DATA import SLANG

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def extract_slang(sentence):
    slang_lis = []
    __entities = []
    final_sen = sentence.replace("\n","")+"."
    string = final_sen.replace("!"," ").replace("."," ").replace("?"," ").split(" ")
    i = -1
    for idx,words in enumerate(string):
        if words in SLANG:
            slang_lis.append(words)
    for z in slang_lis:
        #print(z)
        #print(SLANG[z])
        j = i + 1
        i = sentence.find(z,j)
        __entities.append({
            "value": z,
            "mean": SLANG[z],
            "str_span": [i,i+len(z)]
        })
    return __entities

def main():
    named_entities = []
    input_file = codecs.open('slang_question.txt', encoding='utf-8')
    for line in input_file:
        #logger.info('string converted to utf-8')
        named_entities.append({
                "tags": extract_slang(line),
                "sentence": line
                })
    logger.debug('%s',np.array(named_entities))
    input_file.close()
    #logger.info('file closed')

    input_file = codecs.open('slang_ans.txt', encoding='utf-8')
    #logger.info('testing file open')
    correct = 0
    total = 0
    for i,words in enumerate(input_file):
        word_lis = words.rstrip().split(',')
        for j,word in enumerate(word_lis):
            total += 1
            if len(named_entities[i]['tags']) == len(word_lis):
                if named_entities[i]['tags'][j]['value'] == word:
                    correct += 1
                elif word == '' and len(named_entities[i]['tags']) == 0:
                    correct += 1
    input_file.close()
    logger.debug('Accuracy: {c1}% ({c2} out of {c3})'.format(c1=100*correct/total,c2=correct,c3=total))


if __name__=="__main__":
    main()
    '''
    ans = {}
    st = []
    input_file = codecs.open("slangdict.csv",encoding="utf-8")
    for line in input_file:
        st = line.strip().split(',')
        ans[st[0]]=st[1]
    print(ans)
    '''
