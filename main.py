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
    data = load_data('filename')
    clusterMethod = 'get user input'
    clusterResults = clustering(clusterMethod)
    grade = cluster_grader(clusterResults) # will also create a plot comparing clustering grade to random clustering
    plot_trees() ## can be repeated for multiple clustering methods if necessary, will print true tree and cluster based tree
    return

if __name__ == '__main__':
    main()
