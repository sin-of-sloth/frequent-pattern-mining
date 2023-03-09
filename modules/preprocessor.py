"""
Module that takes care of preprocessing the papers data
"""

###############################################################
# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING #
#                                                             #
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - ARJUN LAL       #
###############################################################

from modules import utils, constants


class PreProcessor:
    """
    Class which handles preprocessing of the paper titles data
    """

    def __init__(self):
        """
        Constructor with default value(s)
        """
        self.PAPERS_FILE = constants.PAPERS_FILE
        self.VOCAB_FILE = constants.VOCAB_FILE
        self.TITLE_VECTOR_FILE = constants.TITLE_VECTOR_FILE
        self.vocab = []
        self.word_vectors = []

    def preprocess_papers(self):
        """
        Preprocesses the paper titles data by creating a vocabulary
        and the file's word vector and writing them to corresponding
        files
        :return:        null
        """
        papers = self.generate_vocab(self.PAPERS_FILE)
        utils.write_list_to_file(self.VOCAB_FILE, papers)
        word_vector = self.get_word_vector(
            self.PAPERS_FILE,
            self.vocab
        )
        utils.write_list_to_file(self.TITLE_VECTOR_FILE, word_vector)

    def generate_vocab(self, filename):
        """
        Generates a vocabulary from a file, where each line in the
        file is of the format:
        `paper_id term1 term2 ... termN`

        :param filename:    path to the file containing papers
        :return:            vocabulary of the papers as a list
        """
        file = open(filename, 'r')
        vocab = []
        for line in file:
            vocab += line.split()[1:]
        vocab = list(dict.fromkeys(vocab))
        self.vocab = vocab
        return vocab

    def get_word_vector(self, filename, vocab):
        """
        Creates a word vector, given a `papers file` and it's `vocabulary`;
        each line in `papers file` of the format:
        `paper_id term1 term2 ... termN`

        :param filename:    path to the file containing papers
        :param vocab:       vocabulary of the papers
        :return:            word vector as a list, where each element is a string
                            of the format
                            `[M] [term_id1]:[count] [term_id2]:[count] ... [term_idN]:[count]`,
                            where [M] is the count of unique terms in the title and
                            [term_idK] is the index of the title's Kth term in the vocabulary
        """
        file = open(filename, 'r')
        word_vectors = []
        for line in file:
            paper = line.split()
            paper_terms = paper[1:]
            unique_terms = list(dict.fromkeys(paper_terms))
            unique_terms_count = len(unique_terms)
            title_vector = []
            for term in unique_terms:
                term_count = paper_terms.count(term)
                title_vector.append(f'{self.get_term_index(term, vocab)}:{term_count}')
            word_vectors.append(f'{unique_terms_count} {" ".join(title_vector)}')

        self.word_vectors = word_vectors
        return word_vectors

    @staticmethod
    def get_term_index(term, vocab):
        """
        Returns the index of the `term` given a `vocabulary`

        :param term:        term whose index is to be found out
        :param vocab:       vocabulary
        :return:            index of the `term` in the `vocabulary`
        """
        return vocab.index(term)
