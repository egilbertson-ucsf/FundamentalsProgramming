import scipy.cluster as sc
from io import StringIO
import numpy as np

class Cluster: 
    def __init__(self): ## takes a CNVData matrix. 
        self.trees = []
        self.random_trees=[]
        self.available_methods = ['single','complete','average',
                                  'weighted','ward','median','centroid']
        
    def cluster(self,data,method=None):
        ## try to load the method. 
        if method:
            try:
                self.available_methods.index(method)
            except ValueError:
                raise Exception('Selected clustering method not available.')
        else:
            method = 'ward'
        
        
        rand = data.copy()
        
        for x in range(0,100):
            self.trees.append(
                self.cluster_single(data.sample(data.shape[1],replace=True,axis=1),method)
            )
            
            self.random_trees.append(
                self.cluster_single(self.generate_random(rand,data.values.max(),(data.values==0).sum()),method)
            )
                    
        return self.trees,self.random_trees

    def cluster_single(self,data,method):
        link = sc.hierarchy.linkage(data,method)
        tree = sc.hierarchy.to_tree(link)
        cluster_newick = self.getNewick(tree, "", tree.dist, data.index)
        cluster_phylo = bp.read(StringIO(cluster_newick),'newick')
        return(cluster_phylo)

    
    def getNewick(self,node, newick, parentdist, leaf_names):
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

        
        