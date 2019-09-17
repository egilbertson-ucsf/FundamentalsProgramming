#!/usr/bin/env python

## Import the data files
def cleanup(string,n=10000):
    return(string.replace('"','').replace('\n','').split(',',))

path_to_data_folder = '/Users/student/Documents/fundamentals/programming/data/'

## Expression data
with open(path_to_data_folder +'E-MTAB-7365.csv') as f:
    expdata_raw= [cleanup(x) for x in f.readlines()]

## Read in cluster file and apply generic cleaning function
with open(path_to_data_folder + 'E-MTAB-7365.clusters.csv') as f:
    clusters_raw = [cleanup(x) for x in f.readlines()]

## obtain gene and cell IDs
expdata_cell_ids = expdata_raw[0]
expdata_gene_ids = [x[0] for x in expdata_raw[1:]]

cell_to_expression_map = {}
for pos,cell_id in enumerate(expdata_cell_ids):
    expvalues = [0 if x[1:][pos] == '' else float(x[1:][pos]) for x in expdata_raw[1:]]
    cell_to_expression_map[cell_id] = expvalues


## Quick and dirty way to get the correct # of clusters
cluster_cell_ids = clusters_raw[0][2:] ## Skip first two columns

k_pos = [x[0] for x in clusters_raw[1:]].index('True') ## Search for the position of "true" in k.sel

k = int(clusters_raw[1:][k_pos][1]) ## get that value of k

selected_clusters = clusters_raw[1:][k_pos][2:-1] ## get selected clusters, drop final row of 0's

clusters = [i for i in range(1,k+1)] ## define all clusters

## calculate the average expression in each cluster.
average_expression_in_cluster = []
for clust_id in clusters:
    ## Identify cells in cluster
    cells_in_cluster = []
    for pos,entry in enumerate(selected_clusters):
        if int(entry)==int(clust_id):
            cells_in_cluster.append(cluster_cell_ids[pos]) ## look up cell using position in table.
    
    ## Obtain expression list for each cell using cell_to_expression map 
    expression_by_cells_in_cluster = [cell_to_expression_map[cell] for cell in cells_in_cluster]
    
    ## Calculate average across cells for each gene (x is vector of exp. per gene across cells.)
    average_expression_in_cluster.append([sum(x)/len(x) for x in list(zip(*expression_by_cells_in_cluster))])
    

    
## transpose averaverage_expression_in_clusters, to be gene x cluster, and zip w/ cluster IDs
## then turn the whole thing into a dictionary using gene IDs
## final data structure, gene_ids --> cluster --> expression
final = dict(zip(expdata_gene_ids,
                 [dict(zip(clusters,x)) for x in zip(*average_expression_in_cluster)]
            ))

## Also reversed:
## final_rev data structure, cluster --> gene_ids --> expression
final_rev = dict(zip(clusters,
    [dict(zip(expdata_gene_ids,x)) for x in average_expression_in_cluster]
   ))


## Example:
print(final['ENSMUSG00000000001'][1] == final_rev[1]['ENSMUSG00000000001'])
