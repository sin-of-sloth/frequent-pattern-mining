"""
Module that mines frequent patterns, maximal patterns, and closed patterns
"""

###############################################################
# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING #
#                                                             #
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - ARJUN LAL       #
###############################################################

import copy

from modules import utils, constants
from modules.apriori import Apriori


class PatternMiner:

    def __init__(self, topic):
        """
        Constructor with default value(s);
        """
        self.freq_k_itemsets = {}
        self.freq_patterns = {}
        self.max_patterns = {}
        self.closed_patterns = {}
        self.TOPIC_FILE_TEMPLATE = constants.TOPIC_FILE_TEMPLATE
        self.topic = topic
        self.FREQ_PATTERN_FILE_TEMPLATE = constants.FREQ_PATTERN_FILE_TEMPLATE
        self.MAX_PATTERN_FILE_TEMPLATE = constants.MAX_PATTERN_FILE_TEMPLATE
        self.CLOSED_PATTERN_FILE_TEMPLATE = constants.CLOSED_PATTERN_FILE_TEMPLATE

    def mine_patterns(self):
        """
        Mines the frequent, maximal, and closed patterns for the topic
        """
        self.mine_frequent_patterns(self.topic)
        self.mine_max_patterns(self.topic)
        self.mine_closed_patterns(self.topic)

    def mine_frequent_patterns(self, topic_num):
        """
        Mines the frequent patterns from the topic's transaction db

        :param topic_num:           an integer, the topic number
        :return:                    null
        """
        topic_file = self.TOPIC_FILE_TEMPLATE.format(topic_num=topic_num)
        apriori = Apriori(topic_file)
        apriori.apriori()

        self.freq_k_itemsets = apriori.frequent_k_itemsets
        self.freq_patterns = self.frequent_k_itemsets_to_freq_itemsets(
            apriori.frequent_k_itemsets
        )
        output_file = self.FREQ_PATTERN_FILE_TEMPLATE.format(topic_num=topic_num)
        self.pattern_to_file(output_file, self.freq_patterns)

    def mine_max_patterns(self, topic_num):
        """
        Mines the maximal patterns from the topic's transaction db

        :param topic_num:           an integer, the topic number
        :return:                    null
        """
        max_itemsets = copy.deepcopy(self.freq_k_itemsets)
        for k, itemsets in self.freq_k_itemsets.items():
            if k + 1 not in self.freq_k_itemsets.keys():
                break
            k_itemsets = [
                itemset.split(' ')
                for itemset in itemsets.keys()
            ]
            next_k_itemsets = [
                itemset.split(' ')
                for itemset in self.freq_k_itemsets[k + 1].keys()
            ]
            for itemset in k_itemsets:
                itemset_key = ' '.join(itemset)
                for next_itemset in next_k_itemsets:
                    if set(itemset).issubset(next_itemset):
                        del max_itemsets[k][itemset_key]
                        break

        self.max_patterns = self.frequent_k_itemsets_to_freq_itemsets(max_itemsets)
        output_file = self.MAX_PATTERN_FILE_TEMPLATE.format(topic_num=topic_num)
        self.pattern_to_file(output_file, self.max_patterns)

    def mine_closed_patterns(self, topic_num):
        """
        Mines the closed patterns from the topic's transaction db

        :param topic_num:           an integer, the topic number
        :return:                    null
        """
        closed_itemsets = copy.deepcopy(self.freq_k_itemsets)
        for k, itemsets in self.freq_k_itemsets.items():
            if k + 1 not in self.freq_k_itemsets.keys():
                break
            k_itemsets = [
                itemset.split(' ')
                for itemset in itemsets.keys()
            ]
            next_k_itemsets = [
                itemset.split(' ')
                for itemset in self.freq_k_itemsets[k + 1].keys()
            ]
            for itemset in k_itemsets:
                itemset_key = ' '.join(itemset)
                itemset_sup = self.freq_k_itemsets[k][itemset_key]
                for next_itemset in next_k_itemsets:
                    next_itemset_key = ' '.join(next_itemset)
                    next_itemset_sup = self.freq_k_itemsets[k + 1][next_itemset_key]
                    if (
                        set(itemset).issubset(next_itemset)
                        and itemset_sup == next_itemset_sup
                    ):
                        del closed_itemsets[k][itemset_key]
                        break

        self.closed_patterns = self.frequent_k_itemsets_to_freq_itemsets(closed_itemsets)
        output_file = self.CLOSED_PATTERN_FILE_TEMPLATE.format(topic_num=topic_num)
        self.pattern_to_file(output_file, self.closed_patterns)

    @staticmethod
    def frequent_k_itemsets_to_freq_itemsets(frequent_k_itemsets):
        """
        Converts a dict of itemsets of format {k: {k-itemset: support, ...}, ...}
        to a dict of itemsets of format {k-itemset: support, ...}

        :param frequent_k_itemsets:     dict of k-itemsets of format {k: {k-itemset: support, ...}, ...}
        :return:                        dict of itemsets of format {k-itemset: support, ...}
        """
        return {
            itemset: support
            for _, itemsets in frequent_k_itemsets.items()
            for itemset, support in itemsets.items()
        }

    @staticmethod
    def pattern_to_file(filename, freq_patterns):
        """
        Writes a set of frequent patterns of format {itemset: support, ...} to the specified file,
        sorting them by decreasing value of support

        :param filename:                file to be written to
        :param freq_patterns:           dict of frequent patterns
        :return:                        null
        """
        utils.write_list_to_file(
            filename,
            [
                f'{support} {itemset}'
                for itemset, support in sorted(
                    freq_patterns.items(),
                    key=lambda item: item[1],
                    reverse=True
                )
            ]
        )
