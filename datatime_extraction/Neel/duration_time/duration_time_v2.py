import re
import numpy as np
def extract_unit_time(sentence):
    matches = re.finditer(r'[\W0-9](minute[s]?|day[s]?|year[s]?|hour[s]|month[s]?|(milli|micro|nano|pento|femto|pico)?second[s]?|min[s]?|yr[s]?|hr[s]?|sec[s]?|millennia|millennium|century|centuries|semester[s]?|quarter[s]?|trimaster[s]?|season[s]?|decade[s]?|week[s]?|wk[s]?|th[s]?|pm[.]?|am[.]?|p.m[.]?|a.m[.]?|lunar.month[s]?|leap.year[s]?|leap.second[s]?|later|late|high.noon|half.life|greenwich.mean.time|galactic.year|fortnight|delayed|delay|decennium|daytime[s]?|daylight[s]?|cuckoo.clock?|chronological?|chronology?|chronometer?|clock[s]?|calendar.year[s]?|bicentennial?|biennial?|belated?|bedtime?|ante.meridian[s]?|anytime?|annual?|midnight?|midmorning?|moment[s]?|nighttime?|on.time?|premature?|present?|schedule[s]?|season?|someday[s]?|sometime[s]?|soon?|sunrise?|sunset?|tonight?|today?|tomorrow?|twilight?|early?|everyday?)[\W]|[0-9]+[\ ]*([s])[\W$]',sentence, re.IGNORECASE)
    entities = []
    for m in matches:
        obj = {'amount':'','unit':'','str_span':[m.start(),m.end()]}
        for idx, g in enumerate(m.groups()):
            if g != None:
                if idx in [3,5]:
                    obj['unit'] = g
        obj['amount'] = m.group(0).replace(obj['unit'],'').strip()
        entities.append(obj)
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
                if ((named_entities[i]['tags'][j]['amount'] == tag) or (named_entities[i]['tags'][j]['unit'] == tag)):
                    correct += 1
            elif tag == '' and len(named_entities[i]['tags']) == 0:
                correct += 1
    print 'Accuracy: {}% ({} out of {})'.format(100*correct/total,correct,total)
