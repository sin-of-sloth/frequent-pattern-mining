"""
Module containing some utility functions
"""

###############################################################
# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING #
#                                                             #
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - ARJUN LAL       #
###############################################################

import math


def write_list_to_file(filename: str, content: list):
    """
    Writes each element of the list on a new line in the given file

    :param filename:        path to file to which list is to be written
    :param content:         list to be written
    :return:                null
    """
    file = open(filename, 'w')
    file.write('\n'.join(content))


def read_file_to_list(filename: str):
    """
    Returns a list, where each element is a line in the given file

    :param filename:        path to the file to be read
    :return:                list of lines in the file
    """
    file = open(filename, 'r')
    content = file.read()
    return content.split('\n')


def stringlist_to_listlist(strings: list):
    """
    Converts a list of strings to a list of lists, where each sublist
    is the string split by spaces

    :param strings:         list of strings
    :return:                list of lists
    """
    return [
        string.split(' ')
        for string in strings
    ]


def pattern_file_to_phrase_file(filename, vocab):
    """
    Converts a pattern file into a phrase file, by mapping
    pattern items to corresponding word in the vocabulary

    :param filename:        the pattern file
    :param vocab:           the vocabulary of the patterns
    :return:                null
    """
    phrase_filename = f'{filename}.phrase'
    phrase_content = []
    contents = read_file_to_list(filename)
    for line in contents:
        items = line.split(' ')
        phrase = []
        for item in items:
            try:
                phrase.append(vocab[int(item)])
            except ValueError:
                phrase.append(item)
        phrase_content.append(' '.join(phrase))
    write_list_to_file(phrase_filename, phrase_content)


def sigmoid(x):
    """
    Calculates f(x), where f(x) is the sigmoid function,
    f(x) = 1 / (1 + e^(-x))
    :param x:               real number
    :return:                sigmoid value
    """
    return 1 / (1 + math.exp(-x))

