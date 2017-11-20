import re
import numpy as np
def extract_unit_time(sentence):
    sentence = ' {} '.format(sentence)
    matches = re.finditer(r'[\W0-9](minute[s]?|day[s]?|year[s]?|hour[s]|month[s]?|(milli|micro|nano|pento|femto)?second[s]?|min[s]?|yr[s]?|hr[s]?|sec[s]?|millennia|millennium|century|centuries|semester[s]?|quarter[s]?|trimaster[s]?|season[s]?|decade[s]?|week[s]?|wk[s]?)[\W]|[0-9]+[\ ]*([s])[\W$]',sentence, re.IGNORECASE)
    entities = []
    for m in matches:
        for idx, g in enumerate(m.groups()):
            if g != None:
                entities.append({
                    "value": g,
                    "str_span": [m.start(idx+1)-1,m.end(idx+1)-1]
                })
                break
    return entities

named_entities = []
with open('time_unit.txt') as f:
    for sentence in f:
        named_entities.append({
            "sentence":sentence,
            "tags": extract_unit_time(sentence)
        })
    print np.array(named_entities)

with open('time_unit_keys.txt') as f:
    correct = 0
    total = 0
    for i,tags in enumerate(f):
        tags = tags.rstrip().lower().split(',')
        for j, tag in enumerate(tags):
            total += 1
            if len(named_entities[i]['tags']) == len(tags):
                if named_entities[i]['tags'][j]['value'] == tag:
                    correct += 1
            elif tag == '' and len(named_entities[i]['tags']) == 0:
                correct += 1
    print 'Accuracy: {}% ({} out of {})'.format(100*correct/total,correct,total)
