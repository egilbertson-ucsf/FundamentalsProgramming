import scipy.cluster as sc
from io import StringIO
import numpy as np

class Cluster: 
    """
    """
    def __init__(self): ## takes a CNVData matrix. 
        self.trees = []
        self.clust_ids=[]
        self.random_trees=[]
        self.random_clust_ids=[]
        self.available_methods = ['single','complete','average',
                                  'weighted','ward','median','centroid']
        
    def cluster(self,data,n_bootstraps=100,method=None,distance_metric='Euclidean'):
        """   
        Function to use 

        """
        ## try to load the method. 
        if method:
            try:
                self.available_methods.index(method)
            except ValueError:
                raise Exception('Selected clustering method not available.')
        else:
            method = 'ward'
        
        
        rand = data.copy()
        num_zeroes = (data.values==0).sum()
        val_max = data.values.max()
 
        for x in range(0,100):
            
            boot_tree, boot_clust_id = self.cluster_single(data.sample(data.shape[1],replace=True,axis=1),method)
            
            ## Append bootstrapped tree and cluster ID to required lists 
            self.trees.append(boot_tree)
            self.clust_ids.append(boot_clust_id)
            
            rand_tree, rand_clust_id = self.cluster_single(self.generate_random(rand,val_max,num_zeroes),method)
            
            ## Append random tree and cluster ID to required lists
            self.random_trees.append(rand_tree)
            self.random_clust_ids.append(rand_clust_id)
                    
        return self.trees, self.random_trees, self.clust_ids, self.random_clust_ids

    def cluster_single(self,data,method):
        link = sc.hierarchy.linkage(data,method)
        tree = sc.hierarchy.to_tree(link)
        
        cluster_id = dict(zip(data.index,sc.hierarchy.cut_tree(link,n_clusters=4).T.tolist()[0]))
        
        cluster_newick = self.getNewick(tree, "", tree.dist, data.index)
        cluster_phylo = bp.read(StringIO(cluster_newick),'newick')
        return cluster_phylo, cluster_id

    
    def getNewick(self,node, newick, parentdist, leaf_names):
        """
        Function to 
        """
        if node.is_leaf():
            return "%s:%.2f%s" % (leaf_names[node.id], parentdist - node.dist, newick)
        else:
            if len(newick) > 0:
                newick = "):%.2f%s" % (parentdist - node.dist, newick)
            else:
                newick = ");"
            newick = self.getNewick(node.get_left(), newick, node.dist, leaf_names)
            newick = self.getNewick(node.get_right(), ",%s" % (newick), node.dist, leaf_names)
            newick = "(%s" % (newick)
            return newick
        
    def generate_random(self,rm,maxval,zeroes):
        randarray = np.random.random_sample(rm.values.size)*maxval
        randarray[np.random.choice(np.arange(0,rm.values.size-1),zeroes,replace=False)] = 0
        rm.iloc[:,:] = randarray.reshape(rm.shape)
        return(rm)