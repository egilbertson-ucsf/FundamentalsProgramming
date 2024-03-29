import scipy.cluster as sc
from io import StringIO
import numpy as np
import Bio.Phylo as bp

class Cluster:
    """
    Class that implements a clustering interface for CNV data. This class takes in a CNV data matrix generated by load_data.py and can calculate the clustering result of various agglomerative clustering strategies. The metric and method for determing linkage can be specified. Generated trees can be returned as Newick format, Bio.Phylo tree structures. Hierachical trees are cut to generate 4 clusters. 
    
    Attributes:
        self.trees (list): A list object containing n_boostraps number of trees generated by agglomerative clustering
        
        self.clust_ids (list): A list object containing n_boostraps dictionaries, each dictionary mapping species to cluster identity.
        
        self.random_trees (list): A list object containing n_boostraps number of random trees generated by agglomerative clustering on a random matrix.
        
        self.random_clust_ids(list): A list object containing n_boostraps dictionaries, each dictionary mapping species to cluster identity generated from random clustering.
        
        self.available_methods (list): A list of available clustering methods, adapted from scipy.hierachical.clustering
        
        self.available_metrics (list): A list of available clustering distance metrics, adapted from scipy.spatial.distance.pdist.
    
    """

    def __init__(self):
        """
        Constructor for the Cluster data class. Initializes storage variables.
        
        Parameters:
            None
        
        """

        self.trees = []
        self.clust_ids=[]
        self.random_trees=[]
        self.random_clust_ids=[]
        self.available_methods = ['single','complete','average',
                                  'weighted','ward','median','centroid']       
        self.available_metrics = ['braycurtis', 'canberra', 'chebyshev', 
                                  'cityblock', 'correlation', 'cosine', 'dice', 
                                  'euclidean', 'hamming', 'jaccard', 'jensenshannon', 
                                  'kulsinski', 'mahalanobis', 'matching', 'minkowski', 
                                  'rogerstanimoto', 'russellrao', 'seuclidean', 
                                  'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule']
        
    def cluster(self,data,method=None,metric=None,n_bootstraps=100):
        """   
        Interface function for clustering the CNV data matrix. 
        
        Parameters:
            data (pandas.DataFrame): A pandas DataFrame containing the CNV data matrix, with species as rows, and genes as columns. For this specific data-set, there are 91 species and 6491 orthologous genes across the 91 species. 
            
            method (string): A string indicating the clustering method to use. Validted against self.available_methods
            
            metric (string): A string indicating the distance metric  to use. Validted against self.available_metrics
            
            n_bootstraps (int): An int indicating the number of bootstraps to perform on the data to generate a tree.
            
            
        Returns:
            self.trees (list): A list object containing n_boostraps number of trees generated by agglomerative clustering
        
            self.clust_ids (list): A list object containing n_boostraps dictionaries, each dictionary mapping species to cluster identity.
            
            self.random_trees (list): A list object containing n_boostraps number of random trees generated by agglomerative clustering on a random matrix.
        
            self.random_clust_ids(list): A list object containing n_boostraps dictionaries, each dictionary mapping species to cluster identity generated from random clustering.
                

        """
        
        ## try to load the method.
        if method:
            try:
                self.available_methods.index(method)
            except ValueError:
                raise Exception('Selected clustering method not available.')
        else:
            method = 'ward'
            
        
        ## try to load the metric
        if metric:
            try:
                self.available_metrics.index(metric)
            except ValueError:
                raise Exception('Selected distance metric not available.')
        else:
            metric = 'euclidean'
        
        
        rand = data.copy()
        num_zeroes = (data.values==0).sum()
        val_max = data.values.max()
 
        ## Iterate over the number of boostraps
        for x in range(0,n_bootstraps):
            
            ## Cluster on the bootstrapped tree
            boot_tree, boot_clust_id = self.cluster_single(data.sample(data.shape[1],replace=True,axis=1),method,metric)
            
            self.trees.append(boot_tree)
            self.clust_ids.append(boot_clust_id)
            
            ## Cluster on the random tree
            rand_tree, rand_clust_id = self.cluster_single(self.generate_random(rand,val_max,num_zeroes),method,metric)
            
            self.random_trees.append(rand_tree)
            self.random_clust_ids.append(rand_clust_id)

        return self.trees, self.random_trees, self.clust_ids, self.random_clust_ids

    def cluster_single(self,data,method,metric):
        """
        Function to perform a single clustering, using scipy.hierachical. 
        
        Parameters:
            data (pandas.DataFrame): A pandas DataFrame containing the CNV data matrix, with species as rows, and genes as columns. For this specific data-set, there are 91 species and 6491 orthologous genes across the 91 species. 
            
            method (string): A string indicating the clustering method to use. Validted against self.available_methods
            
            metric (string): A string indicating the distance metric  to use. Validted against self.available_metrics
        
        Returns:
            cluster_phylo (Bio.Phylo.Tree): A hierachical tree genrated by agglomerative clustering, stored in a Bio.Phylo tree class.
            cluster_id (list): A dictionary mapping species (tree terminal leaves) with their assumed cluster. Generated by cutting the cluster_phylo tree to generate 4 clusters. 
        
        """
        link = sc.hierarchy.linkage(data,method,metric)
        tree = sc.hierarchy.to_tree(link)

        cluster_id = dict(zip(data.index,sc.hierarchy.cut_tree(link,n_clusters=4).T.tolist()[0]))

        cluster_newick = self.getNewick(tree, "", tree.dist, data.index)
        cluster_phylo = bp.read(StringIO(cluster_newick),'newick')
        return cluster_phylo, cluster_id


    def getNewick(self,node, newick, parentdist, leaf_names):
        """
        Function to transform a scipy tree to a Newick format string, used to facilitate the conversion of the clustered result to a Bio.Phylo.Tree object. This function uses tail recusion to generate the newick string. 
        
        Parameters:
            newick (string): A newick representation of the Tree node considered.
            parentdist (float): The distance to the parent node. 
            leaf_names (list): A list of leaf nodes to be recursed on. 
        
        
        Returns:
            newick (string): A newick representation of the Tree node considered.
        
        """
        ## If the node is a leaf,return
        if node.is_leaf():
            return "%s:%.2f%s" % (leaf_names[node.id], parentdist - node.dist, newick)
        else:
            ## otherwise, recurse left / right
            if len(newick) > 0:
                newick = "):%.2f%s" % (parentdist - node.dist, newick)
            else:
                newick = ");"
            newick = self.getNewick(node.get_left(), newick, node.dist, leaf_names)
            newick = self.getNewick(node.get_right(), ",%s" % (newick), node.dist, leaf_names)
            newick = "(%s" % (newick)
            return newick

    def generate_random(self,rm,maxval,zeroes):
        """
        Function to replace the entries of a CNV data matrix with an approximately similar zero-inflated distribution.
        
        Parameters:
            rm (pandas.DataFrame): A copy of the CNV data matrix DataFrame.
            maxval (float): The maximum number in the CNV data matrix DataFrame
            zeroes (int): The number of zeroes present in the oringal CNV data matrix.
        
        """
        ## generate a number of random samples in the range of the data-set.
        randarray = np.random.random_sample(rm.values.size)*maxval 
        
        ## Select number zeroes of those entries, and randomly set to zero.
        randarray[np.random.choice(np.arange(0,rm.values.size-1),zeroes,replace=False)] = 0
        rm.iloc[:,:] = randarray.reshape(rm.shape)
        return(rm)
