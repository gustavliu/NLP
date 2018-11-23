# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import yscale, xscale, title, plot
import re
from collections import Counter
from functools import reduce
from operator import mul, add


filename = '.\\data\\zh_wiki_00'


def read_data():
    all_content = open(filename, 'r', encoding='UTF-8').read()
    return all_content


def tokenize(string):
    return ''.join(re.findall('[\w|\d]+', string))


def get_data():
    data = read_data()
    return tokenize(data)


def plot_m(M, all_character_counts):
    yscale('log')
    xscale('log')
    title('Frequency of n-th most frequent word and 1/n line.')
    plot([c for (w, c) in all_character_counts.most_common()])
    plot([M/i for i in range(1, len(all_character_counts)+1)])


def get_probability_from_counts(count):
    all_occurences = sum(count.values())
    min_occurence = min(count.values())
    def get_prob(item):
        return count.get(item, min_occurence) / all_occurences
    return get_prob


def get_running_time(func, arg, times):
    start_time = time.time()
    for _ in range(times):
        func(arg)
    print('\t\t {} used time is {}'.format(func.__name__, time.time() - start_time))


def get_char_probability(char):
    all_occurences = sum(all_character_counts.values())
    return all_character_counts[char] / all_occurences


def prob_of_string(string, get_char_prob):
    return reduce(mul, [get_char_prob(c) for c in string])


def get_2_gram_prob(prob, word, prev):
    if prob(word+prev) > 0:
        return prob(word+prev) / prob(prev)
    else:
        return prob(word)


def get_2_gram_string_prob(prob_fun, string):
    probablities = []
    for i, c in enumerate(string):
        prev = '<s>' if i == 0 else string[i-1]
        probablities.append(get_2_gram_prob(prob_fun, c, prev))
    return reduce(mul, probablities)


string_pair = ['发表了重要的讲话', '发表了重要的僵化']


if __name__ == '__main__':
    all_data = get_data()
    # all_character_counts = Counter(all_data)
    # get_char_prob = get_probability_from_counts(all_character_counts)
    gram_length = 2
    two_gram_counts = \
        Counter(all_data[i:i + gram_length] for i in range(len(all_data) - gram_length))
    get_pair_prob = get_probability_from_counts(two_gram_counts)
    str1 = get_2_gram_string_prob(get_pair_prob, string_pair[0])
    str2 = get_2_gram_string_prob(get_pair_prob, string_pair[1])
    # M = all_character_counts.most_common()[0][1]
    # plot_m(M, all_character_counts)
    # plt.show()
    # get_char_prob = get_probability_from_counts(all_character_counts)
    # get_running_time(get_char_probability, '神', 10000)
    # get_running_time(get_char_prob, '神', 10000)
    print(str1)
    print(str2)
