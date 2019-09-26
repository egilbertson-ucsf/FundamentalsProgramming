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
    pass

def main():
    import_functions()

    clusterMethod = 'get user input'
    
    true_tree = ld.TrueTree().load_true_tree('data/phyliptree.phy')
    data = ld.CNVData().readCNVMatrix('data/LS_blastn_Gar_noDenom.txt')
    trees,random_trees = cl.Cluster().cluster(data,'ward')
    
    grade = cluster_grader(clusterResults) 
    plot_trees() ## can be repeated for multiple clustering methods if necessary, will print true tree and cluster based tree
    return

if __name__ == '__main__':
    main()
