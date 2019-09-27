#!/usr/bin/env python3
import argparse
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
    argument_parser.add_argument("method",type=str,nargs='?',metavar='method',default='ward',
                                 help="Specify an aggolmerative clustering method for reconstructing the phylogeny. Ex. 'ward'")

    ## Add argument for metrics
    argument_parser.add_argument("-m","--metric",dest='metric',default='euclidean',
                                 help="Specify the distance metric used. Ex. 'euclidean'")

    ## Add argument for bootstraps
    argument_parser.add_argument("-b","--bootstraps", type= int, dest='n_bootstraps',default=50,
                                 help="Specify the number of bootstrap resamplings of the data matrix. Default is 100.")


    argument_parser.add_argument("-l","--list",action='store_true',dest='list_methods',default=False,
                                 help="Lists available clustering methods / distance metrics")
    ## Parse arguments
    args = argument_parser.parse_args()

    print(args.method)

    if args.list_methods:
        cobj = cl.Cluster()
        print("Available Methods:")
        print("    "+", ".join(cobj.available_methods))
        print("Available Distance Metrics:")
        print("    "+", ".join(cobj.available_metrics))

    else:
        print("Loading data...")
        true_tree = ld.TrueTree().load_true_tree('data/phyliptree.phy')
        data = ld.CNVData().readCNVMatrix('data/LS_blastn_Gar_noDenom.txt')

        print("Clustering and reconstructing phylogeny...")
        trees, random_trees, clust_ids, random_clust_ids = cl.Cluster().cluster(data,args.method,args.metric,args.n_bootstraps)

        print("Scoring clusters...")
        ari_clusters, ari_random = cg(data.index, trees, random_trees, clust_ids,random_clust_ids,true_tree)

        ari_clusters, ari_random = cg(data.index, trees, random_trees, clust_ids,random_clust_ids,true_tree)
        ac=pd.Series(ari_clusters)
        plt.plot_trees(true_tree, trees[ac.idxmax()])
        plt.plot_dist(ari_random, ari_clusters)

    exit()
    return

if __name__ == '__main__':
    main()
