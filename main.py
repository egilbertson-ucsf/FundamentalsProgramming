import load_data as ld
import cluster as cl

def import_functions():
    ## importing all our other things that we write
    """
    External files to write

    data loading:
        read in data matrix and clean up naming etc.

    clustering:
        given a clustering method/s do clustering algorithm specified on data matrix
        output

    cluster gradings:
        grade cluster tree compared to true tree

    trees:
        tree class
        tree plotting


    """
    from cluster_grading import grade as cg
    from phylotree import plot_trees
    import load_data as ld
    import cluster as cl
    import phylotree as plt

def main():
    import_functions()

    cluster_method = str(input('Choose a clustering method from [single, complete, average, weighted, ward, median, centroid]: '))

    true_tree = ld.TrueTree().load_true_tree('data/phyliptree.phy')
    data = ld.CNVData().readCNVMatrix('data/LS_blastn_Gar_noDenom.txt')
    trees,random_trees,clust_ids, random_clust_ids = cl.Cluster().cluster(data,cluster_method)

    ari_clusters, ari_random = cg(data.index, trees, random_trees, clust_ids,random_clust_ids,true_tree)
    ac=pd.Series(ari_clusters)
    plt.plot_trees(true_tree, trees[ac.idxmax()])
    plt.plot_dist(ari_random, ari_cluster)

    return
if __name__ == '__main__':
    main()
