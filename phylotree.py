import Bio.Phylo as bp
import matplotlib.pyplot as plt
import pandas as pd
def plot_trees(true_tree, best_clust_tree):
    print('True Tree')
    bp.draw_ascii(true_tree)
    print('Best Clustering Based Tree')
    bp.draw_ascii(best_clust_tree)
    return


def plot_dist(random, cluster):
    data = pd.DataFrame(random).join(cluster)
    plt.boxplot(data=data)
    return
