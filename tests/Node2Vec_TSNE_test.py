from tests.utils import *

from embedding_tests.Node2VecTest import Node2VecTest
from visualizing_tests.TSNETest import TSNETest

def Node2Vec_TSNE_test():

    i = get_index()

    if i == 1:
        print_block("Test 1: wiki edgeset")
        edgeset = "./datasets/wiki/wiki_edgelist.txt"
        featureset = "./datasets/wiki/wiki_labels.txt"
        location = "./images/wiki/wiki_Node2Vec_TSNE_1.jpg"
    
    elif i == 2:
        print_block("Test 2: hr2 edgeset")
        edgeset = "./datasets/hr2/hr2_edgelist.txt"
        featureset = "./datasets/hr2/hr2_labels.txt"
        location = "./images/hr2/hr2_Node2Vec_TSNE_1.jpg"

    elif i == 3:
        print_block("Test 3: lock edgeset")
        edgeset = "./datasets/lock/lock_edgelist.txt"
        featureset = "./datasets/lock/lock_labels.txt"
        location = "./images/lock/lock_Node2Vec_TSNE_1.jpg"
    
    else:
        print("Test of index {} currently unavailable.".format(i))
        return
        
    node2vec = Node2VecTest(edgeset, featureset=featureset, walk_length=10, num_walks=80, p=0.25, q=4, workers=1, window_size=5, iter=3)
    tsne = TSNETest(node2vec.embeddings, node2vec.has_feature, location, n_components=2, verbose=1, random_state=0)
    show_evaluation_results(node2vec, tsne)