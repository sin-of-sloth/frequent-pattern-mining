"""
Driver program for HW1; calls necessary module methods for given tasks
"""

###############################################################
# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING #
#                                                             #
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - ARJUN LAL       #
###############################################################

from modules.preprocessor import PreProcessor
from modules.partitioner import Partitioner
from modules.pattern_miner import PatternMiner
from modules.purity import PurityRanker
from modules import utils, constants


def main():
    # preprocess the papers data
    print('Pre processing papers')
    preprocessor = PreProcessor()
    preprocessor.preprocess_papers()

    # run lda program to assign topics to terms
    # $ lda-c-dist/lda est 0.001 5 lda-c-dist/settings.txt title.txt random result/

    # re-organize terms by topics
    print('Partitioning by topics')
    partitioner = Partitioner()
    partitioner.partition()

    # mine frequent patterns
    print('Mining frequent, maximal, and closed patterns by topic')
    frequent_patterns = {}
    for topic in range(constants.TYPES_OF_TOPICS):
        pattern_miner = PatternMiner(topic)
        pattern_miner.mine_patterns()
        frequent_patterns[topic] = pattern_miner.freq_patterns

    # re rank by purity
    print('Re ranking by purity')
    purity_ranker = PurityRanker()
    purity_ranker.rank_by_purity(frequent_patterns)

    # generate phrase files
    vocab = utils.read_file_to_list(constants.VOCAB_FILE)
    for template in constants.TO_BE_PHRASED:
        for topic in range(constants.TYPES_OF_TOPICS):
            filename = template.format(topic_num=topic)
            utils.pattern_file_to_phrase_file(filename, vocab)


if __name__ == '__main__':
    main()
