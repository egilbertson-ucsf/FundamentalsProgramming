import Bio.Phylo as bp
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_trees(true_tree, best_clust_tree):

    '''
    Function to print both a true tree and a tree based on clutering methods to the command line
    The tree will print in ascii format

    Input: two tree object
    Product: Ascii formatted trees printed to terminal interface

    no returned object
    '''
    print('True Tree')
    bp.draw_ascii(true_tree)
    print('Best Clustering Based Tree')
    bp.draw_ascii(best_clust_tree)
    return


def plot_dist(random, cluster):
    '''
    Function to boxplot the distributions of our clustering method (*100) scores
    next to random clustering scores

    Input: two lists of adjusted rand index scores 
    Product: boxplot

    no returned object
    '''
    rand = pd.Series(random)
    clust = pd.Series(cluster)
    dist = pd.DataFrame(pd.concat([rand,clust], axis=1))
    dist.columns = ['Random','Clustered']

    sns.boxplot(x="variable", y="value", data=pd.melt(dist))
    plt.ylabel('Adjusted Rand Index')
    plt.xlabel('Method')
    plt.show()
    return
