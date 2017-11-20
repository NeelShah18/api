import re
import emoji
import numpy as np
import codecs
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def extract_emojis(string):
    __entities = []
    for pos,c in enumerate(string):
        if c in emoji.UNICODE_EMOJI:
            logger.info('Extraction function open')
            __entities.append({
                "value": c,
                "str_span":[pos,pos],
                "mean" : emoji.demojize(c, delimiters=(" __", "__ "))
                })
            logger.info('Extraction function closed')
            
    return __entities

def main():
    named_entities = []
    input_file = codecs.open('emoji_data.txt', encoding='utf-8')
    logger.info('file opened')
    for line in input_file:
        assert type(line)==unicode
        logger.info('string converted to utf-8')
        named_entities.append({
                "sentence": line,
                "tags": extract_emojis(line)
                })
        logger.info('emoji extractor complete')
    logger.debug('%s',np.array(named_entities))
    input_file.close()
    logger.info('file closed')

    input_file = codecs.open('emoji_ans.txt', encoding='utf-8')
    logger.info('testing file open')
    correct = 0
    total = 0
    for i,words in enumerate(input_file):
        assert type(line)==unicode
        word_lis = words.rstrip().split(',')
        for j,word in enumerate(word_lis):
            total += 1
            if len(named_entities[i]['tags']) == len(word_lis):
                if named_entities[i]['tags'][j]['value'] == word:
                    correct += 1
                elif word == '' and len(named_entities[i]['tags']) == 0:
                    correct += 1
    input_file.close()
    logger.info('testing file closed')
    logger.debug('Accuracy: %s (%s out of %s)',str(100*correct/total),str(correct),str(total))
    #print 'Accuracy: {}% ({} out of {})'.format(100*correct/total,correct,total)

if __name__=="__main__":
    main()
