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
    import cluster_grading.grade as cg
    from phylotree import plot_trees
    import load_data as ld
    import cluster as cl

def main():
    import_functions()

    cluster_method = str(input('Choose a clustering method from [single, complete, average, weighted, ward, median, centroid]: '))

    true_tree = ld.TrueTree().load_true_tree('data/phyliptree.phy')
    data = ld.CNVData().readCNVMatrix('data/LS_blastn_Gar_noDenom.txt')
    trees,random_trees,clust_ids, random_clust_ids = cl.Cluster().cluster(data,cluster_method)

    ari_clusters, ari_random = cg(data.index, trees, random_trees, clust_ids,random_clust_ids,true_tree)
    plot_trees() ## can be repeated for multiple clustering methods if necessary, will print true tree and cluster based tree
    return

if __name__ == '__main__':
    main()
