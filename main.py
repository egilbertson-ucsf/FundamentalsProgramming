from cluster_grading import grade as cg
from phylotree import plot_trees
import load_data as ld
import cluster as cl
import phylotree as plt
import scipy.cluster as sc
from io import StringIO
import numpy as np
import Bio.Phylo as bp
import pandas as pd

def main():
    argument_parser=argparse.ArgumentParser()

    ## Add argument for clustering method
    argument_parser.add_argument("method",type=str,nargs="+",metavar='Agglomerative clustering method',
                                 help="Specify an aggolmerative clustering method for reconstructing the phylogeny. Ex. 'ward'")

    ## Add argument for metrics
    argument_parser.add_argument("-m","--metric",dest='cluster',default='euclidean',
                                 help="Specify the distance metric used. Ex. 'euclidean'")

    ## Add argument for bootstraps
    argument_parser.add_argument("-b","--bootstraps", dest='n_bootstraps',default=100,
                                 help="Specify the number of bootstrap resamplings of the data matrix. Default is 100.")

    ## Parse arguments
    args = argument_parser.parse_args()
    
    true_tree = ld.TrueTree().load_true_tree('data/phyliptree.phy')
    data = ld.CNVData().readCNVMatrix('data/LS_blastn_Gar_noDenom.txt')
   
    trees, random_trees, clust_ids, random_clust_ids = cl.Cluster().cluster(data,args.method,args.metric,args.bootstraps)

    ari_clusters, ari_random = cg(data.index, trees, random_trees, clust_ids,random_clust_ids,true_tree)

    ari_clusters, ari_random = cg(data.index, trees, random_trees, clust_ids,random_clust_ids,true_tree)
    ac=pd.Series(ari_clusters)
    plt.plot_trees(true_tree, trees[ac.idxmax()])
    plt.plot_dist(ari_random, ari_clusters)

    exit()
    return
  
  
if __name__ == '__main__':
    main()
