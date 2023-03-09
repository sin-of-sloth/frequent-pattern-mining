"""
Module containing constants used
"""

###############################################################
# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING #
#                                                             #
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - ARJUN LAL       #
###############################################################

MIN_SUP = 0.01

TYPES_OF_TOPICS = 5

# relevant files
PAPERS_FILE = 'paper.txt'
VOCAB_FILE = 'vocab.txt'
TITLE_VECTOR_FILE = 'title.txt'
WORD_ASSIGNMENTS_FILE = 'result/word-assignments.dat'

# file name templates
TOPIC_FILE_TEMPLATE = 'topic-{topic_num}.txt'
FREQ_PATTERN_FILE_TEMPLATE = 'patterns/pattern-{topic_num}.txt'
MAX_PATTERN_FILE_TEMPLATE = 'max/max-{topic_num}.txt'
CLOSED_PATTERN_FILE_TEMPLATE = 'closed/closed-{topic_num}.txt'
PURITY_FILE_TEMPLATE = 'purity/purity-{topic_num}.txt'

TO_BE_PHRASED = [
    FREQ_PATTERN_FILE_TEMPLATE,
    MAX_PATTERN_FILE_TEMPLATE,
    CLOSED_PATTERN_FILE_TEMPLATE,
    PURITY_FILE_TEMPLATE,
]
