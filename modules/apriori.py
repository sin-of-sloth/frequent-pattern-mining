"""
Module implementing the apriori algorithm
"""
import copy
###############################################################
# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING #
#                                                             #
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - ARJUN LAL       #
###############################################################

from collections import Counter

from modules import utils, constants
from itertools import combinations


class Apriori:
    """
    Implements the apriori algorithm on a transaction db
    """

    def __init__(self, transaction_file):
        """
        Constructor with default value(s);
        """
        self.transaction_file = transaction_file
        self.transaction_db = self.get_transaction_db(transaction_file)
        self.total_transactions = len(self.transaction_db)
        self.min_sup = constants.MIN_SUP
        self.frequent_k_itemsets = {}

    def apriori(self):
        """
        Implements the apriori algorithm on the transaction db.
        Steps involved are:
            get frequent 1-itemset from transaction db
            repeat while candidates are not empty:
                generate k+1 length candidate itemsets from frequent k-itemsets
                prune candidates whose subsets are not frequent
                test the final set of candidates and get frequent k+1-itemsets
                set k = k + 1

        :return:                null
        """
        frequent_one_itemset = self.get_frequent_one_itemset(self.transaction_db)
        k = 1
        k_length_itemset = frequent_one_itemset
        while k_length_itemset:
            self.frequent_k_itemsets[k] = k_length_itemset
            k += 1
            prev_frequent_k_itemset = utils.stringlist_to_listlist(list(k_length_itemset.keys()))
            candidate_itemsets = self.generate_candidate_itemsets(
                prev_frequent_k_itemset, k
            )
            pruned_candidates = self.prune_candidate_itemsets(
                candidate_itemsets, prev_frequent_k_itemset, k - 1
            )
            k_length_itemset = self.get_frequent_itemset(pruned_candidates)

    @staticmethod
    def generate_candidate_itemsets(itemset, k):
        """
        Generates a list of candidate itemsets of length k, given a list of itemsets,
        by taking the union of each element in the given itemset

        :param itemset:         list of itemsets
        :param k:               length of new candidates
        :return:                candidate itemset
        """
        candidate_sets = [
            set(i + j)
            for i in itemset for j in itemset
            if len(set(i + j)) == k
        ]
        candidates = []
        # Candidates after removing duplicates
        [
            candidates.append(candidate)
            for candidate in candidate_sets
            if candidate not in candidates
        ]
        return candidates

    @staticmethod
    def prune_candidate_itemsets(candidate_itemsets, prev_frequent_itemset, prev_k):
        """
        Prunes a list of candidate itemsets by removing candidates if all their
        subsets are not frequent

        :param candidate_itemsets:      list of candidate k-itemsets
        :param prev_frequent_itemset:   frequent k-1 itemsets
        :param prev_k:                  k - 1
        :return:                        list of pruned candidates
        """
        pruned_candidates = copy.deepcopy(candidate_itemsets)
        for itemset in candidate_itemsets:
            subsets = [list(set(comb)) for comb in combinations(itemset, prev_k)]
            for subset in subsets:
                if subset not in prev_frequent_itemset:
                    pruned_candidates.remove(itemset)
                    break
        return pruned_candidates

    def get_frequent_itemset(self, itemset):
        """
        Returns a list of frequent itemsets from the given itemset list

        :param itemset:         list of candidate itemsets
        :return:                frequent itemsets
        """
        items_with_counts = {}
        for item in itemset:
            for transaction in self.transaction_db:
                if set(item).issubset(transaction):
                    item_key = ' '.join(item)
                    if item_key in items_with_counts:
                        items_with_counts[item_key] += 1
                    else:
                        items_with_counts[item_key] = 1

        frequent_itemsets = {
            item: self.get_support(frequency)
            for item, frequency in items_with_counts.items()
            if self.get_support(frequency) > self.min_sup
        }
        return frequent_itemsets

    def get_frequent_one_itemset(self, transaction_db):
        """
        Returns a list of frequent 1-itemsets in the transaction db

        :param transaction_db:      the transaction db
        :return:                    frequent 1-itemsets
        """
        all_transactions = sum(transaction_db, [])
        return {
            item: self.get_support(frequency)
            for item, frequency in Counter(all_transactions).items()
            if self.get_support(frequency) > self.min_sup
        }

    def get_support(self, frequency):
        """
        Returns the support given a frequency;
        support = frequency / total_transactions

        :param frequency:           frequency of an item
        :return:                    the support of the item in the transaction db
        """
        return frequency / self.total_transactions

    @staticmethod
    def get_transaction_db(transaction_file):
        """
        Creates a transaction db as a list of lists of transactions (items)

        :param transaction_file:    the transaction file
        :return:                    list of lists, each sublist is a list of items
        """
        transactions = utils.read_file_to_list(transaction_file)
        return [
            transaction.split(' ')
            for transaction in transactions
        ]
