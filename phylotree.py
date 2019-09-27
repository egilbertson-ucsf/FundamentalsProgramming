import Bio.Phylo as bp
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_trees(true_tree, best_clust_tree):
    print('True Tree')
    bp.draw_ascii(true_tree)
    print('Best Clustering Based Tree')
    bp.draw_ascii(best_clust_tree)
    return


def plot_dist(random, cluster):
    rand = pd.Series(random)
    clust = pd.Series(cluster)
    dist = pd.DataFrame(pd.concat([rand,clust], axis=1))
    dist.columns = ['Random','Clustered']

    sns.boxplot(x="variable", y="value", data=pd.melt(dist))
    plt.ylabel('Adjusted Rand Index')
    plt.xlabel('Method')
    plt.show()
    return
