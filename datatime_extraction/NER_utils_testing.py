# -*- coding: utf-8 -*-
from __future__ import division

import sys, os

def test_ner_parser__presentation_for_long_sentences(dataset, recognize_function=None ,verbose = True):
    '''
    :function_parser: function that takes string sentence and return list of  ner_objects
    :param
    :dataset: test_dataset
    :function: recognize_function
    :return: accuracy
    '''
    good, bad = 0, 0
    for test in dataset:

        try:
            ner_object = recognize_function(test[0])
            # print "ner_object ", ner_object
            val = [ d['val'] for d in ner_object]
            indices = [ d['str_span'] for d in ner_object]
            # print ner_objects
            # print indices

            if ner_object == test[1]:
                print  test[0]
                print test[1]
                good += 1
                print good
                print "     *****'\x1b[6;30;42m'good'\x1b[0m'****      \n____________________________________________________________________________________"

        except Exception as e:
            print e

    for test in dataset:

        # try:

        ner_object = recognize_function(test[0])
        # print "ner_object ", ner_object
        vals = [ d['val'] for d in ner_object]
        indices = [ d['str_span'] for d in ner_object]

        if ner_object != test[1]:
            bad += 1
            # print
            print "________________________________________________________________________________________________________________"
            print  test[0]
            print "____________________"

            print "ner_objects true:"
            for dt in test[1]:
                print "        ", dt
            print "ner_objects results:"
            for dt in ner_object:
                print "        ", dt, "    -"+test[0][dt['str_span'][0]:dt['str_span'][1]]+ "-"
            print "____________________"
            recognize_function(test[0],verbose=True)
            print "     *****'\033[1;41m'bad'\x1b[0m'****      \n____________________________________________________________________________________"

        # except Exception as e:
        #     exc_type, exc_obj, exc_tb = sys.exc_info()
        #     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        #     print(exc_type, fname, exc_tb.tb_lineno)
        #     bad += 1
        #     print e
        #     print "     *****'\033[1;41m'bad'\x1b[0m'****      \n____________________________________________________________________________________"


    accuracy = good / (good + bad)
    print "accuracy:", 100 * accuracy, " %"
    return accuracy
