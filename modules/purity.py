"""
Module that implements finding the purity of patterns
"""

###############################################################
# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING #
#                                                             #
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - ARJUN LAL       #
###############################################################

import copy
import re
from math import log2

from modules import utils, constants


class PurityRanker:

    def __init__(self):
        """
        Constructor with default value(s);
        """
        self.WORD_ASSIGNMENTS_FILE = constants.WORD_ASSIGNMENTS_FILE
        self.PURITY_FILE_TEMPLATE = constants.PURITY_FILE_TEMPLATE

    def rank_by_purity(self, topicwise_freq_patterns):
        """
        Re ranks a set of frequent patterns based on a score calculated
        using purity and support.

        :param topicwise_freq_patterns:     dict of frequent patterns indexed by topic
        :return:                            null
        """
        topicwise_pattern_purity = copy.deepcopy(topicwise_freq_patterns)
        topicwise_docs = {
            topic: [
                itemset.split(' ')
                for itemset in utils.read_file_to_list(constants.TOPIC_FILE_TEMPLATE.format(topic_num=topic))
            ]
            for topic in topicwise_freq_patterns.keys()
        }
        doc_topics = self.get_doc_topics()
        for topic, freq_patterns in topicwise_freq_patterns.items():
            topic_docs = topicwise_docs[topic]
            other_topics = [
                t
                for t in topicwise_freq_patterns.keys()
                if t != topic
            ]
            dt_size = len(topic_docs)
            other_topic_pattern_sups = {}
            other_topic_dtts = {}
            for pattern_str, support in freq_patterns.items():
                pattern = pattern_str.split(' ')
                for other_topic in other_topics:
                    other_topic_docs = topicwise_docs[other_topic]
                    other_topic_pattern_freq = 0
                    for other_itemset in topicwise_docs[other_topic]:
                        if set(pattern).issubset(other_itemset):
                            other_topic_pattern_freq += 1

                    other_topic_pattern_sups[other_topic] = self.get_support(
                        other_topic_pattern_freq,
                        len(other_topic_docs)
                    )
                    other_topic_dtts[other_topic] = self.get_dtt_size(
                        topic, other_topic, doc_topics
                    )

                topicwise_pattern_purity[topic][pattern_str] = self.calculate_purity(
                    support, dt_size, other_topics, other_topic_pattern_sups, other_topic_dtts
                )

            filename = self.PURITY_FILE_TEMPLATE.format(topic_num=topic)
            self.pattern_to_file(filename, topicwise_pattern_purity[topic], topicwise_freq_patterns[topic])

    def get_doc_topics(self):
        """
        Creates a list of lists, where each list has the set of topics
        that have been assigned to a document's words
        :return:                    list of lists of format
                                [[topic1, topic2, ...], [topic1, topic2, ...], ...]
        """
        word_assignment_regex = r'[0-9]+:[0-9]+'
        doc_topics = []
        for topic_word_assignments in utils.read_file_to_list(self.WORD_ASSIGNMENTS_FILE):
            word_assignments = re.findall(
                word_assignment_regex, topic_word_assignments
            )
            doc_word_topics = []
            for word_assignment in word_assignments:
                _, topic = self.get_word_and_topic(word_assignment)
                doc_word_topics.append(topic)
            doc_topics.append(list(set(doc_word_topics)))

        return doc_topics

    @staticmethod
    def calculate_purity(support, dt_size, other_topics, other_topic_pattern_sups, other_topic_dtts):
        """
        Purity of pattern p in topic t calculated using-
        purity(p, t) = log[f (t, p)/|D(t)|] − log(max[(f (t, p) + f (t′, p))/|D(t, t′)|])
        where,
            f(t, p) is the frequency of pattern p appearing in topic t (i.e., support of p in topic t)
            D(t) = {d|topic t is assigned to at least one word in document d}
            D(t, t′) is the union of D(t) and D(t′)

        :param support:                     f(t, p)
        :param dt_size:                     |D(t)|
        :param other_topics:                list of t'
        :param other_topic_pattern_sups:    dict of {t' : f(t', p)}
        :param other_topic_dtts:            dict of {t' : D(t, t')}
        :return:                            purity(t, p)
        """
        return (
                log2(support / dt_size)
                -
                log2(
                    max(
                        [
                            (
                                    (support + other_topic_pattern_sups[other_topic])
                                    /
                                    other_topic_dtts[other_topic]
                            )
                            for other_topic in other_topics
                        ]
                    )
                )
        )

    @staticmethod
    def get_dtt_size(topic1, topic2, doc_topics):
        """
        Returns the size of the set D(topic1, topic2) defined as
        D(t, t') = {d | either topic t or topic t' is assigned to at least one word in doc d}

        :param topic1:              topic 2
        :param topic2:              topic 1
        :param doc_topics:          list of lists, each sublist is the topics assigned to a doc's words
        :return:                    size of the set D(topic1, topic2)
        """
        dtt_size = 0
        for doc_topic in doc_topics:
            if topic1 in doc_topic or topic2 in doc_topic:
                dtt_size += 1

        return dtt_size

    @staticmethod
    def get_support(frequency, total_transactions):
        """
        Returns the support given a frequency;
        support = frequency / total_transactions

        :param frequency:           frequency of an item
        :param total_transactions:  total transactions in the db
        :return:                    the support of the item in the transaction db
        """
        return frequency / total_transactions

    @staticmethod
    def get_word_and_topic(word_assignment):
        """
        Given a word assignment of the form `word:topic`, returns the
        `word` as string and `topic` as an int

        :param word_assignment:         word assignment
        :return:                        word (str) and topic (int)
        """
        word = word_assignment.split(':')[0]
        topic = int(word_assignment.split(':')[1])
        return word, topic

    def pattern_to_file(self, filename, pattern_purities, pattern_supports):
        """
        Writes the patterns to file in decreasing order by a score based on
        each pattern's purity and support

        :param filename:                file to be written to
        :param pattern_purities:        dict of {itemset: purity}
        :param pattern_supports:        dict of {itemset: support}
        :return:                        null
        """
        utils.write_list_to_file(
            filename,
            [
                f'{purity} {itemset}'
                for itemset, purity in sorted(
                    pattern_purities.items(),
                    key=lambda item: self.calculate_score(item[1], pattern_supports[item[0]]),
                    reverse=True
                )
            ]
        )

    @staticmethod
    def calculate_score(purity, support):
        """
        Calculates score based on support and purity, defined as:
        score(support, purity) = support ∗ σ(purity)
        where σ(x) is the sigmoid function, σ(x) = 1 / (1 + e^(-x))

        :param purity:                  purity of a pattern
        :param support:                 support of a pattern
        :return:                        score for the pattern
        """
        return support * utils.sigmoid(purity)
