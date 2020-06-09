###
### This module will perform pattern match on a given text using Rabin Karb and KMP  Algorithm.
### Author : Delhi Durai
###


import tracemalloc
import json
from plotter import plotter
from time import process_time
#
# Constant defined for Rabin Karp
#
NUMBER_OF_CHARACTERS = 256
SOME_PRIME_NUMBER = 127

#
# This method finds the longest prefix from the 0th index and allocates the index to the long_prefix_suffix
# array
#
def get_long_prefixsuffix(pattern, pattern_len):
    len = 0
    long_prefix_suffix= [0]*pattern_len
    i = 1

    while i < pattern_len:
        if pattern[i]== pattern[len]:
            len += 1
            long_prefix_suffix[i] = len
            i += 1
        else:
            if len != 0:
                len = long_prefix_suffix[len-1]
            else:
                long_prefix_suffix[i] = 0
                i += 1
    return long_prefix_suffix

#
# This method uses KMP Algorithm to search for a pattern in the given text.
# If the pattern matches with the text, this method will return the index of the text where the pattern is matched.
#

def kmp_pattern_match(pattern, act_txt):
    pattern_len = len(pattern)
    text_len = len(act_txt)
    b_pattern_found = False
    j = 0
    long_prefix_suffix = get_long_prefixsuffix(pattern, pattern_len)
    i = 0
    pattern_count = 0
    while i < text_len:
        if pattern[j] == act_txt[i]:
            i += 1
            j += 1
        if j == pattern_len:
            b_pattern_found = True
            print("Pattern found at index " + str(i-j))
            pattern_count+=1
            j = long_prefix_suffix[j-1]
        elif i < text_len and pattern[j] != act_txt[i]:
            if j != 0:
                j = long_prefix_suffix[j-1]
            else:
                i += 1

    if pattern_count >0:
        print ("Number of places the pattern occurred  " + str(pattern_count))
    if not b_pattern_found:
        print("The Pattern {} not found in the given text {}".format(pattern,act_txt))

#
# This method uses Rabin Karp Algorithm to search for a pattern in the given text.
# If the pattern matches with the text, this method will return the index of the text where the pattern is matched.
#
def rabin_karp(pattern,act_txt):
    # initialize variables
    pattern_len = len(pattern)
    b_pattern_found = False
    text_len = len(act_txt)
    pattern_hash = 0
    text_hash = 0
    h = 1

    for indx in range(pattern_len-1):
        h = (h * NUMBER_OF_CHARACTERS)% SOME_PRIME_NUMBER

    for indx in range(pattern_len):
        pattern_hash = (NUMBER_OF_CHARACTERS * pattern_hash + ord(pattern[indx]))% SOME_PRIME_NUMBER
        text_hash = (NUMBER_OF_CHARACTERS * text_hash + ord(act_txt[indx]))% SOME_PRIME_NUMBER
    pattern_count = 0
    for indx in range(text_len-pattern_len + 1):
        if pattern_hash == text_hash:
            for intrnl_indx in range(pattern_len):
                if act_txt[indx + intrnl_indx] != pattern[intrnl_indx]:
                    break
            intrnl_indx+= 1
            if intrnl_indx == pattern_len:
                b_pattern_found = True
                pattern_count+=1
                print ("Pattern found at index " + str(indx))
        if indx < text_len-pattern_len:
            text_hash = (NUMBER_OF_CHARACTERS*(text_hash-ord(act_txt[indx])*h) + ord(act_txt[indx + pattern_len]))% SOME_PRIME_NUMBER
            if text_hash < 0:
                text_hash = text_hash + SOME_PRIME_NUMBER
    if pattern_count >0:
        print ("Number of places the pattern occurred  " + str(pattern_count))
    if not b_pattern_found:
        print("The Pattern {} not found in the given text {}".format(pattern,act_txt))

#
# Function to read the given file
#
def readfile(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

#
# Test method to test the pattern implementation.
# Takes json file which contains the input text and the search pattern.
# The boolean is_rabin, controls which algorithm to call. If it is true Rabin Karp is called, when false KMP is called.
# is_fixed_pattern when true will provide analysis graph for fixed pattern. When false provides analysis graph for fixed input text
#

def simulate_test(is_rabin, is_fixed_pattern, filename):

    data_dict = readfile(filename)
    p = plotter();
    tracemalloc.start()

    for data in data_dict:
        t1_start = process_time()
        text = data["text"]
        pattern = data["pattern"]
        p.add_pattern(pattern)
        p.add_txt(text)
        print("Text size {}, Pattern size {}".format(len(text), len(pattern)))
        if(is_rabin):
            rabin_karp(pattern, text)
        else:
            kmp_pattern_match(pattern, text)
        current, peak = tracemalloc.get_traced_memory()
        p.add_usage(current / 10**6)
        print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
        t1_stop = process_time()
        time = t1_stop-t1_start
        print(f"Time taken to complete {time}ms")
        p.add_time(time)
    tracemalloc.stop()

    if is_fixed_pattern:
        p.plot_txt_time()
        p.plot_txt_size()
    else:
        p.plot_pat_time()
        p.plot_pat_size()




# Test simulation 1:- Rabin Karp, fixed pattern size and varying text input size.
simulate_test(True,True, "patternfile.json")
# Test simulation 2:- KMP, fixed pattern size and varying text input size.
simulate_test(False,True, "patternfile.json")
# Test simulation 3:- KMP, varying pattern size and fixed text input size.
simulate_test(True,False, "patternfile_2.json")
# Test simulation 4:- KMP, varying pattern size and fixed text input size.
simulate_test(False,False, "patternfile_2.json")


