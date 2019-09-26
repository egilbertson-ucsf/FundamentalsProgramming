## Loading / clustering data functions
import pandas as pd
import Bio.Phylo as bp
import scipy as sc

class TrueTree:
    def __init__(self):
        self.true_tree = []
    def load_true_tree(self,file_path):
        self.true_tree = bp.read(file_path,'newick')
        return(self.true_tree)
        
class CNVData:
    def __init__(self):
        self.CNVData = []
        self.label_replace_dictionary = {
        'SM1_centroids_nucleotides': 'Chelydra_serpentina',
        'SM2_centroids_nucleotides': 'Anolis_sagrei',
        'SM3_centroids_nucleotides': 'Elgaria_multicarinata',
        'SM4_centroids_nucleotides': 'Lamprophis',
        'SM5_centroids_nucleotides': 'Agkistrodon_piscivorus',
        'SM6_centroids_nucleotides': 'Xenopeltis_unicolor',
        'SM7_centroids_nucleotides': 'Alligator_mississippiensis',
        'SM8_centroids_nucleotides': 'Sceloporus_undulatus',
        'SM9_centroids_nucleotides': 'Pogona',
        'SM10_centroids_nucleotides': 'Sternotherus_odoratus',
        'SM11_centroids_nucleotides': 'Sternotherus_odoratus',
        'SM12_centroids_nucleotides': 'Scincella_lateralis',
        'SM13_centroids_nucleotides': 'Terrapene_carolina',
        'SM14_centroids_nucleotides': 'Agkistrodon_piscivorus',
        'SM15_centroids_nucleotides': 'Eublepharis_macularius',
        'TC_centroids_nucleotides': 'Thamnophis_sirtalis',
        'HS08_centroids_nucleotides': 'Thamnophis_elegans',
        'HS11_centroids_nucleotides': 'Thamnophis_couchii'
        }

    
    def readCNVMatrix(self,file_path):
        ## Read in data-file using Pandas. Assume TSV. Use column 1 as index. 
        ## Transpose so genes are columns. 
        self.CNVData = pd.read_csv(file_path,sep='\t', index_col=0).transpose()
        
        ## Drop unneccesary Column counting total CNV per species
        self.CNVData = self.CNVData.drop(['Total'])
        ## Replace NaN entries --> 0
        self.CNVData.fillna(0,inplace=True) 
        
        ## Min/max scaling of copy number
        self.CNVData = (self.CNVData - self.CNVData.min()) / (self.CNVData.max()-self.CNVData.min()) ## Min-max transform
        
        ## Replace NaN entries --> 0
        self.CNVData.fillna(0,inplace=True) 
        
      
        ## Relabel species names to line up with 'true' tree
        self.CNVData.index = self.relabelIndex(self.CNVData.index)
        
        return(self.CNVData)
    
    def relabelIndex(self,labels):
       # correct names 
        fixed_labels = []

        for label in labels:
            if label in self.label_replace_dictionary:
                fixed_labels.append(self.label_replace_dictionary[label])
            else:
                fixed_labels.append(label)
        return(fixed_labels)