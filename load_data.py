## Loading / clustering data functions
import pandas as pd
import Bio.Phylo as bp
import scipy as sc

class TrueTree:
    """
    Data-like class meant to load the True Tree from the .phy file accompanying this package.
    
    Attributes:
        true_tree (Bio.Phylo.Tree): The true tree stored in a Bio.Phylo tree class.
    """
    
    def __init__(self):
        """
        Constructor for TrueTree data class.
        
        Paramters:
            None
        """
        self.true_tree = []
        
    def load_true_tree(self,file_path):
        """
        Function to load and parse the true tree, and store it.
        
        Parameters:
            file_path (string): A valid file path to the true tree .phy file
         
        Returns:
            Bio.Phylo.Tree: A Bio.Phylo Tree class storing the true tree.
        """
        self.true_tree = bp.read(file_path,'newick')
        return(self.true_tree)
        
class CNVData:
    """
    Data-like class meant to store a Species by Gene matrix with entries corresponding to gene Copy Number. A specific datafile is provided for working with reptilian species samples.
    
    Attributes:
        CNVData (pandas.DataFrame): A pandas DataFrame containing the CNV data matrix, with species as rows, and genes as columns. For this specific data-set, there are 91 species and 6491 orthologous genes across the 91 species. 
        
        label_replace_dictionary (dict): A dictionary storing phylogenetically correct names for some species in the given CNV data matrix. 
    """
    def __init__(self):
        """
        Constructor for CNVData data class.
        
        Paramters:
            None
        """
        
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
        """
        Function to read the CNV data matrix from a .tsv file, and parse it correctly. NA's are replaced with 0s, and the copy numbers are min-max normalized across their species as a standardization method. Incorrectly named species are renamed using self.relabelIndex.
        
        Parameters:
            file_path (string): A valid file path to the .tsv CNV data file
            
        Returns:
            self.CNVData (pandas.DataFrame):  A pandas DataFrame containing the CNV data matrix, with species as rows, and genes as columns. For this specific data-set, there are 91 species and 6491 orthologous genes across the 91 species. The copy number values are normalized across species is heavily zero-inflated.
            
        """
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
        """
        Function to relabel the indicies of a pandas DataFrame containing reptile species names with their correct phylogenetic names using the class attribute self.label_replace_dictionary.
        
        Parameters:
            labels (pandas.DataFrame.index): An index of a pandas DataFrame containing reptile species names. Behaves like a list object 
            
        Returns:
            fixed_labels (list): A list object containing the corrected phylogenetic names of reptile species passed in labels.
        
        """
        ## init correct name matrix
        fixed_labels = []

        ## Iterate over the labels
        for label in labels:
            ## if it must be fixed, lookup in label_replace_dictionary and store the fixed name 
            ## or store the name if not.
            if label in self.label_replace_dictionary:
                fixed_labels.append(self.label_replace_dictionary[label])
            else:
                fixed_labels.append(label)
        return(fixed_labels)