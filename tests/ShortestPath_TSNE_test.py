from tests.utils import *

from embedding_tests.ShortestPathTest import ShortestPathTest
from visualizing_tests.TSNETest import TSNETest

def ShortestPath_TSNE_test():

    i = get_index()

    if i == 1:
        print_block("Test 1: wiki edgeset")
        edgeset = "./datasets/wiki/wiki_edgelist.txt"
        featureset = "./datasets/wiki/wiki_labels.txt"
        location = "./images/wiki/wiki_ShortestPath_TSNE_1.jpg"
    
    elif i == 2:
        print_block("Test 2: hr2 edgeset")
        edgeset = "./datasets/hr2/hr2_edgelist.txt"
        featureset = "./datasets/hr2/hr2_labels.txt"
        location = "./images/hr2/hr2_ShortestPath_TSNE_1.jpg"

    elif i == 3:
        print_block("Test 3: lock edgeset")
        edgeset = "./datasets/lock/lock_edgelist.txt"
        featureset = "./datasets/lock/lock_labels.txt"
        location = "./images/lock/lock_ShortestPath_TSNE_1.jpg"
    
    else:
        print("Test of index {} currently unavailable.".format(i))
        return

    shortestpath = ShortestPathTest(edgeset, featureset=featureset)
    tsne = TSNETest(shortestpath.embeddings, shortestpath.has_feature, location, n_components=2, verbose=1, random_state=0)
    show_evaluation_results(shortestpath, tsne)