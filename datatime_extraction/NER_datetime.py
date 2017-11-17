from __future__ import division

from datetime import datetime,timedelta

#
import pytz
# import json
# import copy
# import logging

import regex as re
from dateutil import parser
from dateutil.tz import *
from NER_utils_testing import test_ner_parser__presentation_for_long_sentences

# todo 19th century / third millennium
class PartialDateTime(dict):
    def __init__(self, year=None, month=None, day=None, weekday=None,
                 hour=None, minute=None, second=None,  # microsecond=None,
                 tzname=None, tzoffset=None ):  # ampm=None):
        super(PartialDateTime,self).__init__( year=year, month=month, day=day, weekday=weekday,
                 hour=hour, minute=minute, second=second,  # microsecond=None,
                 tzname=tzname, tzoffset=tzoffset)

    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__

    def __repr__(self):
        dic = self.__dict__
        at_least_one_key = False
        s = ""
        for key in self.keys():  # 'microsecond', 'ampm'
            at_least_one_key = True
            if self[key] != None:
                s += key + "=" + str(self[key]) + ", "
        if at_least_one_key:
            return "PartialDateTime(" + s[:-2] + ")"
        else:
            return "PartialDateTime()"

    # def __str__(self):
    #     dic = self.__dict__
    #     at_least_one_key = False
    #     s = ""
    #     for key in ['year', 'month', 'day', 'weekday', 'hour', 'minute',
    #                 'second', 'tzname', 'tzoffset']:  # 'microsecond', 'ampm'
    #         at_least_one_key = True
    #         if dic[key] != None:
    #             s += key + "=" + str(dic[key]) + ", "
    #     if at_least_one_key:
    #         return "PartialDateTime(" + s[:-2] + ")"
    #     else:
    #         return "PartialDateTime()"


class AfterPartialDateTime(PartialDateTime):
    def __init__(self, dt):
        self.dt = dt


class BeforePartialDateTime(PartialDateTime):
    def __init__(self, dt):
        self.dt = dt


def recognize_datetime(sentence,base_datetime=datetime(2016, 12, 31, 16, 0, 0, 0), verbose=False):
    ORDINAL_PATTERN = '\d+st|\d+th|\d+rd|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|thirtieth'
    DIGITS_PATTERN = '(?<![0-9])(\d+)(?![0-9])'
    year_pattern = '[12]?\d{3}'
    LONG_WEEKDAYS_PATTERN = '(?<![a-z])(monday|tuesday|wednesday|thursday|friday|saturday|sunday|today|yesterday|tomorrow)(?![a-z])'
    ALL_WEEKDAYS_PATTERN = '(?<![a-z])(monday|tuesday|wednesday|thursday|friday|saturday|sunday|mon|tue|tues|wed|thur|thurs|fri|sat|sun|today|yesterday|tomorrow)(?![a-z])'
    MONTHS_PATTERN = '(?<![a-z])(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)(?![a-z])'
    TIMEZONES_PATTERN = '(?<![a-z])(pacific\s+time|eastern\s+time|mountain\s+time|central\s+time|ACDT|ACST|ACT|ACWDT|ACWST|ADDT|ADMT|ADT|AEDT|AEST|AFT|AHDT|AHST|AKDT|AKST|AKTST|AKTT|ALMST|ALMT|AMST|AMT|ANAST|ANAT|ANT|APT|AQTST|AQTT|ARST|ART|ASHST|ASHT|AST|AWDT|AWST|AWT|AZOMT|AZOST|AZOT|AZST|AZT|BAKST|BAKT|BDST|BDT|BEAT|BEAUT|BIOT|BMT|BNT|BORT|BOST|BOT|BRST|BRT|BST|BTT|BURT|CANT|CAPT|CAST|CAT|CAWT|CCT|CDDT|CDT|CEDT|CEMT|CEST|CET|CGST|CGT|CHADT|CHAST|CHDT|CHOST|CHOT|CIST|CKHST|CKT|CLST|CLT|CMT|COST|COT|CPT|CST|CUT|CVST|CVT|CWT|CXT|ChST|DACT|DAVT|DDUT|DFT|DMT|DUSST|DUST|EASST|EAST|EAT|ECT|EDDT|EDT|EEDT|EEST|EET|EGST|EGT|EHDT|EMT|EPT|EST|ET|EWT|FET|FFMT|FJST|FJT|FKST|FKT|FMT|FNST|FNT|FORT|FRUST|FRUT|GALT|GAMT|GBGT|GEST|GET|GFT|GHST|GILT|GIT|GMT|GST|GYT|HAA|HAC|HADT|HAE|HAP|HAR|HAST|HAT|HAY|HDT|HKST|HKT|HLV|HMT|HNA|HNC|HNE|HNP|HNR|HNT|HNY|HOVST|HOVT|HST|ICT|IDDT|IDT|IHST|IMT|IOT|IRDT|IRKST|IRKT|IRST|ISST|IST|JAVT|JCST|JDT|JMT|JST|JWST|KART|KDT|KGST|KGT|KIZST|KIZT|KMT|KOST|KRAST|KRAT|KST|KUYST|KUYT|KWAT|LHDT|LHST|LINT|LKT|LMT|LMT|LMT|LMT|LRT|LST|MADMT|MADST|MADT|MAGST|MAGT|MALST|MALT|MART|MAWT|MDDT|MDST|MDT|MEST|MET|MHT|MIST|MIT|MMT|MOST|MOT|MPT|MSD|MSK|MSM|MST|MUST|MUT|MVT|MWT|MYT|NCST|NCT|NDDT|NDT|NEGT|NEST|NET|NFT|NMT|NOVST|NOVT|NPT|NRT|NST|NT|NUT|NWT|NZDT|NZMT|NZST|OMSST|OMST|ORAST|ORAT|PDDT|PDT|PEST|PET|PETST|PETT|PGT|PHOT|PHST|PHT|PKST|PKT|PLMT|PMDT|PMMT|PMST|PMT|PNT|PONT|PPMT|PPT|PST|PT|PWT|PYST|PYT|QMT|QYZST|QYZT|RET|RMT|ROTT|SAKST|SAKT|SAMT|SAST|SBT|SCT|SDMT|SDT|SET|SGT|SHEST|SHET|SJMT|SLT|SMT|SRET|SRT|SST|STAT|SVEST|SVET|SWAT|SYOT|TAHT|TASST|TAST|TBIST|TBIT|TBMT|TFT|THA|TJT|TKT|TLT|TMT|TOST|TOT|TRST|TRT|TSAT|TVT|ULAST|ULAT|URAST|URAT|UTC|UYHST|UYST|UYT|UZST|UZT|VET|VLAST|VLAT|VOLST|VOLT|VOST|VUST|VUT|WARST|WART|WAST|WAT|WDT|WEDT|WEMT|WEST|WET|WFT|WGST|WGT|WIB|WIT|WITA|WMT|WSDT|WSST|WST|WT|XJT|YAKST|YAKT|YAPT|YDDT|YDT|YEKST|YEKST|YEKT|YEKT|YERST|YERT|YPT|YST|YWT|ZZZ)(?![a-z])'

    ## explicit north american timezones that get replaced
    NA_TIMEZONES_PATTERN = 'pacific|eastern|mountain|central'
    ALL_TIMEZONES_PATTERN = TIMEZONES_PATTERN + '|' + NA_TIMEZONES_PATTERN  ## add (?<![a-z])
    DELIMITERS_PATTERN = '[\s\:\.\,\+\[\]\(\)\-\_\@\/ht]+|at|of'  # [htz]|at|of'  # with space
    TIME_PERIOD_PATTERN = 'am|a\.?m\.?|p\.?m\.?|pm'
    ## can be in date strings but not recognized by dateutils
    EXTRA_TOKENS_PATTERN = 'due|by|on|standard|daylight|savings|time|date|of|to|until|z|t|h|at'  # todo |this\ +year'

    RELATIVE_PATTERN = 'before|after|next|last|ago|in\ the\ following'
    TIME_SHORTHAND_PATTERN = 'noon|midnight'
    UNIT_PATTERN = 'second|minute|hour|day|week|month|year'

    date_time_pattern = """
     (
     (?P<beginning> {ordinal}|{digits}|{weekday}|{month}|{time_shorthand})
     (?P<middle> {ordinal}|{digits}|{weekday}|{month}|{time_period}|{time_shorthand}|{timezone}|{delimiters})*
     (?P<end> {ordinal}|{digits}|{weekday}|{month}|{time_period}|{time_shorthand}|{timezone})
     )
     |
     (
     (in\s+){month}\s*{year}?
     )
     |
     (
     (in\s+|next\s+|last\s+){month}
     )
     |
     # (
     #(next\s+|last\s+){datetime_unit}
     #)
     #|
     (
     {long_weekday}
     )
    """.format(
        digits=DIGITS_PATTERN,
        ordinal=ORDINAL_PATTERN,
        weekday=ALL_WEEKDAYS_PATTERN,
        long_weekday=LONG_WEEKDAYS_PATTERN,
        month=MONTHS_PATTERN,
        time_period=TIME_PERIOD_PATTERN,
        delimiters=DELIMITERS_PATTERN,
        timezone=TIMEZONES_PATTERN,
        time_shorthand=TIME_SHORTHAND_PATTERN,
        year=year_pattern,
        datetime_unit = UNIT_PATTERN)

    regex_datetime = re.compile(date_time_pattern, re.IGNORECASE | re.VERBOSE)

    def preprocess_for_dateutil_parsing(s):
        s = re.sub(r"^[0-9,. ]*$", "", s) # reject 6.12 5.66
        s = re.sub(r"(\d{1,2})(\.|\s+)(\d{1,2})(\.|\s+)(\d{2}\s*('am|a\.?m\.?|p\.?m\.?|pm'))", r"\1:\3:\5", s)  # 5 25 20 am | 5.25.20 am -> 5:25:20am
        s = re.sub(r"(\d{1,2})(\.|\s+)(\d{2}\s*('am|a\.?m\.?|p\.?m\.?|pm'))", r"\1:\3", s)  #5 25 am | 5.25am -> 5:25am
        s = re.sub(r"\d+\s+1\/2", '',  s) # discard 833 1/2
        s = re.sub(r"\d+\s+1\/4", '', s)  # discard 833 1/4
        s = re.sub(r"\d+\s+3\/4", '', s)  # discard 833 3/4
        s = re.sub(r"[@,]", r" ", s) # rm , and @
        s = re.sub(r"(?i)pacific\s+time", r"PST", s)
        s = re.sub(r"(?i)eastern\s+time", r"EST", s)
        s = re.sub(r"(?i)mountain\s+time", r"MST", s)
        s = re.sub(r"(?i)central\s+time", r"CST", s)
        s = re.sub(r"(?i)noon", r"12:00:00", s)
        s = re.sub(r"(?i)midnight", r"00:00:00", s)
        s = re.sub(r"(?i)today", base_datetime.strftime("%Y-%m-%d"), s)
        s = re.sub(r"(?i)tomorrow",  (base_datetime + timedelta(days=1)).strftime("%Y-%m-%d"), s)
        s = re.sub(r"(?i)yesterday", (base_datetime - timedelta(days=1)).strftime("%Y-%m-%d"), s)
        s = re.sub(r"(?i)now", base_datetime.strftime("%Y-%m-%d %H:%M:%S"), s)
        return s

    dates_indices = []
    for match in regex_datetime.finditer(sentence):
        ne = {'val':parser_from_dateutil(preprocess_for_dateutil_parsing(match[0])), 'str_span': match.span(0)}
        if verbose:
            print "\nin recognize_datetime function:",match[0]
            print " after preprocessing: ", preprocess_for_dateutil_parsing(match[0])
            print " found as:",ne
        if ne['val']:
            if verbose:
                print "this ne has 'val' key",ne['val']
            if (not ne['val']['month']) or ( ne['val']['month'] and (ne['val']['month']<=12) and (ne['val']['month']>=1) ):
                if (not ne['val']['day']) or ( ne['val']['day'] and (ne['val']['day'] <= 31) and (ne['val']['day'] >= 1)):
                    dates_indices.append( ne  )
                    if verbose:
                        print "datetime found :", ne['val']

    if verbose:
        print "\nexit final value: ",dates_indices

    return dates_indices


def parser_from_dateutil(string, verbose=False):
    try:
        dt = parser.parse(string, fuzzy=True)
        return dt
    except Exception as e:
        print "Error in function parser_from_dateutil: ", e


def parser_decomp(self, timestr, default=None, ignoretz=False, tzinfos=None, **kwargs):
    # parsing without default:
    # http://stackoverflow.com/questions/8434854/parsing-a-date-in-python-without-using-a-default
    # return self._parse(timestr, **kwargs)
    results = self._parse(timestr, **kwargs)[0]
    if results:
        if results.ampm == 1 and results.hour < 12:
            results.hour += 12
        return PartialDateTime(year=results.year, month=results.month, day=results.day, weekday=results.weekday,
                                hour=results.hour, minute=results.minute, second=results.second,
                                tzname=results.tzname, tzoffset=results.tzoffset)  # ampm=results.ampm)
    else:
        return []


parser.parser.parse = parser_decomp

#######################################################


PartialDateTime_dataset = [
    ## English Dates
    ('may God have mercy on him', []),
    ('we will travel in may 2009',[PartialDateTime(year=2009, month=5)]),
    ('we may travel next may',[PartialDateTime(month=10)]),
    ('[Sept] 04, 2014.', [PartialDateTime(year=2014, month=9, day=4)]),
    ('Tuesday Jul 22, 2014', [PartialDateTime(year=2014, month=7, day=22, weekday=1)]),
    ('10:04am EDT', [PartialDateTime(hour=10, minute=4, tzname='EDT')]),
    ('Friday', [PartialDateTime(weekday=4)]),
    ('November 19, 2014 at noon', [PartialDateTime(year=2014, month=11, day=19, hour=12, minute=0, second=0)]),
    ('December 13, 2014 at midnight', [PartialDateTime(year=2014, month=12, day=14, hour=0, minute=0, second=0)]),
    ('Nov 25 2014 10:17 pm EST', [PartialDateTime(year=2014, month=11, day=25, hour=22, minute=17, tzname='EST')]),
    ('Wed Aug 05 12:00:00 EDT 2015',
     [PartialDateTime(year=2015, month=8, day=5, weekday=2, hour=12, minute=0, second=0, tzname='EDT')]),
    ('April 9, 2013 at 6:11 a.m.', [PartialDateTime(year=2013, month=4, day=9, hour=6, minute=11)]),
    ('Aug. 9, 2012 at 2:57 p.m.', [PartialDateTime(year=2012, month=8, day=9, hour=14, minute=57)]),
    ('December 10, 2014, 11:02:21 pm', [PartialDateTime(year=2014, month=12, day=10, hour=23, minute=2, second=21)]),
    ('8:25 a.m. Dec. 12, 2014', [PartialDateTime(year=2014, month=12, day=12, hour=8, minute=25)]),
    ('2:21 p.m., December 11, 2014', [PartialDateTime(year=2014, month=12, day=11, hour=14, minute=21)]),
    ('Fri, 12 Dec 2014 10:55:50',
     [PartialDateTime(year=2014, month=12, day=12, weekday=4, hour=10, minute=55, second=50)]),
    ('20 Mar 2013 10h11', [PartialDateTime(year=2013, month=3, day=20, hour=10, minute=11)]),
    ('10:06am Dec 11, 2014', [PartialDateTime(year=2014, month=12, day=11, hour=10, minute=6)]),
    ('19 February 2013 year 09:10', [PartialDateTime(year=2013, month=2, day=19), PartialDateTime(hour=9, minute=10)]),

    # Numeric dates
    ('06-17-2014', [PartialDateTime(year=2014, month=6, day=17)]),
    ('13/03/2014', [PartialDateTime(year=2014, month=3, day=13)]),
    ('2016-02-04T20:16:26+00:00',
     [PartialDateTime(year=2016, month=2, day=4, hour=20, minute=16, second=26, tzoffset=0, tzname='UTC')]),
    ('11. 12. 2014, 08:45:39', [PartialDateTime(year=2014, month=11, day=12, hour=8, minute=45, second=39)]),
    ("i am looking for a date june 4th 1996 to july 3rd 2013",
     [PartialDateTime(year=1996, month=6, day=4), PartialDateTime(year=2013, month=7, day=3)]),
    ("2 dates: i am looking for a date june 4th 1996 so july 3rd 2013",
     [PartialDateTime(year=1996, month=6, day=4), PartialDateTime(year=2013, month=7, day=3)]),
    ("2 dates: october 27 1994 to be put into effect on june 1 1995",
     [PartialDateTime(year=1994, month=10, day=27), PartialDateTime(year=1995, month=06, day=1)]),
    ("Today is 25 of September of 2003, exactly at 10:49:41 with timezone -03h",
     [PartialDateTime(year=2016, month=12, day=31), PartialDateTime(year=2003, month=9, day=25),
      PartialDateTime(hour=10, minute=49, second=41)]),
    ("tomorrow at 9am pacific time", [PartialDateTime(year=2017, month=1, day=1, hour=9, tzname='PST')]),
    ('was the trains from delhi late yesterday?', [PartialDateTime(year=2016, month=12, day=30)] ),
    ("Poster 's Site : mitbbs.com BBS (  Wed   Jan   17  10:09:13  2007  )",
     [PartialDateTime(year=2007, month=1, day=17, weekday=2, hour=10, minute=9, second=13)]),
    ("The time has been set for 5:00 p.m. sharp ,  February   11   (   Sunday   )   ,   2007  .",
     [PartialDateTime(hour=17, minute=0), PartialDateTime(year=2007, month=2, day=11, weekday=6)]),
    (
        "When I was back in China  this   year  , I tutored little girls at two relatives homes , feeling  14   -   17  is a very dangerous age group for girls .",
        []),
    (
    "First , according to the Caijing report , Luneng 's privatization process lasted  11   years   (   1995   -   2006   )  . ",
    [PartialDateTime(year=1995), PartialDateTime(year=2006)]),
    ("Jim was playing basketball at 5.25pm PST on Wednesday",[PartialDateTime(hour=17,minute=25, tzname='PST'), PartialDateTime(weekday=2)]),
    ("Jim was playing basketball at 5 25am PST on evening",   [PartialDateTime(hour=5, minute=25, tzname='PST')]),
    ("Jim was playing basketball at 5.25.20pm PST on Wednesday",
     [PartialDateTime(hour=17, minute=25, second=20, tzname='PST'), PartialDateTime(weekday=2)]),
    ("Jim was playing basketball at 5 25 20 am PST on evening", [PartialDateTime(hour=5, minute=25, second=20, tzname='PST')]),
("today", [PartialDateTime(month=12, year=2016, day=31)]),
    ("January 19, 2017 @ 3:45 pm", [PartialDateTime(hour=15, month=1, year=2017, day=19, minute=45)]),
    ("January 8 2017,10.50 am.",[PartialDateTime(minute=50, hour=10, month=1, year=2017, day=8)]),
    ("It was stephane's second visit to Italy with 3 friends in UA414 on January, 19 2017 @3.45.20 pm and spent us$ 10,000.5 which is 60.32% of his income .",[PartialDateTime(hour=15, month=1, second=20, year=2017, day=19, minute=45)]),
("It was stephane's second visit to Italy with 3 friends in UA414 on January, 19 2017 @3.45.20 p.m and spent us$ 10,000.5 which is 6.12% of his income .",[PartialDateTime(hour=15, month=1, second=20, year=2017, day=19, minute=45)]),
    ('6.12%',[]),
    ('7, 500',[]),
    ('today, I am stephane egly and I will cook five eggs at 9:30am for $ 5000 $ in san francisco',[])
    ,('9 1/2',[])

]


if __name__ == '__main__':
    test_ner_parser__presentation_for_long_sentences(dataset=PartialDateTime_dataset,
                                                 recognize_function=recognize_datetime)
    # test_datetime_parser(verbose=False)

    # test_datetime_parser(function_parser=parser_from_dateutil)

    # print datetime_dataset_datetime[-1][0]
    # parser_from_dateutil(string=datetime_dataset_datetime[-1][0], verbose=True)
    #
    #
    # ontonotes_date = training_dataset_from_foldername_subfolder(root_foldername=ontonotes_english_web_folder,
    #                                                             category='DATE',
    #                                                             min_length_sentence=0,
    #                                                             max_length_sentence=1000)
    # from NER_inference import print_tagged_list_of_words
    #
    # cpt = 0
    # for i, labels in enumerate(ontonotes_date[1]):
    #     if set(labels) != set(['O']):
    #         cpt += 1
    #         print cpt
    #         print print_tagged_list_of_words(ontonotes_date[0][i], labels)
    #         sentence = " ".join(ontonotes_date[0][i])
    #         dt_list=recognize_datetime(sentence)
    #         for dt in dt_list:
    #             print dt#,' found in:',sentence[dt[1][0]+1:dt[1][1]-1],"\n"
    #         print "\n"
    # # #
    # ontonotes_date = training_dataset_from_foldername_subfolder(root_foldername=ontonotes_english_web_folder,
    #                                                             category='TIME',
    #                                                             min_length_sentence=0,
    #                                                             max_length_sentence=1000)
    # cpt = 0
    # for i, labels in enumerate(ontonotes_date[1]):
    #     if set(labels) != set(['O']):
    #         cpt += 1
    #         print cpt
    #         print print_tagged_list_of_words(ontonotes_date[0][i], labels)
    #         sentence = " ".join(ontonotes_date[0][i])
    #         print parser_from_regex(sentence)
    #         print "\n"

