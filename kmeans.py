from load_cluster_data import load_data
from cluster_grader import grade
import sklearn.cluster as sk
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np


# Use scikit methods to perform clustering using various approaches
def kmeans(matrix):
    return sk.KMeans(n_clusters=4, random_state=1).fit(matrix)

def ward(matrix):
    return sk.AgglomerativeClustering(n_clusters=4).fit(matrix)

def complete(matrix):
    return sk.AgglomerativeClustering(n_clusters=4, linkage='complete').fit(matrix)

def single(matrix):
    return sk.AgglomerativeClustering(n_clusters=4, linkage='single').fit(matrix)

def average(matrix):
    return sk.AgglomerativeClustering(n_clusters=4, linkage='average').fit(matrix)

def random_cluster(matrix):
    return np.random.randint(4, size=matrix.shape[0])


# Taken from https://stackoverflow.com/questions/28222179/save-dendrogram-to-newick-format
def get_newick(node, newick, parentdist, leaf_names):
    if node.is_leaf():
        return "%s:%.2f%s" % (leaf_names[node.id], parentdist - node.dist, newick)
    else:
        if len(newick) > 0:
            newick = "):%.2f%s" % (parentdist - node.dist, newick)
        else:
            newick = ");"
        newick = get_newick(node.get_left(), newick, node.dist, leaf_names)
        newick = get_newick(node.get_right(), ",%s" % (newick), node.dist, leaf_names)
        newick = "(%s" % (newick)
        return newick


if __name__ == '__main__':
    # Configuration Values
    filename = '..\LS_blastn_Gar_noDenom.txt'
    label_replace_dictionary = {
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

    # Routine
    matrix = load_data(filename, index_dictionary=label_replace_dictionary)
    kmeans_result = kmeans(matrix)
    agglomerative_ward = ward(matrix)
    agglomerative_complete = complete(matrix)
    agglomerative_single = single(matrix)
    agglomerative_average = average(matrix)

    # Generate random clusters 100 times, and show their data
    i = 0
    random_grade_ari = 0
    random_grade_tree = 0
    while i < 100:
        random_result = random_cluster(matrix)
        random_grade = grade(matrix.index, random_result)
        random_grade_ari += random_grade[0]
        random_grade_tree += random_grade[1]
        i += 1
    random_ari_avg = random_grade_ari / 100
    random_tree_avg = random_grade_tree / 100
    

    # Display hierarchy/create newick of hierarchy for best performing algorithm
    linked_ward = linkage(matrix, method='ward')
    # plt.figure(num=None, figsize=(8,6), dpi=160)
    # plt.rc('ytick', labelsize=8)
    
    # dendrogram(linked_ward,
    #            orientation='top',
    #            labels=matrix.index,
    #            distance_sort='descending',
    #            color_threshold=40)
    # plt.show()
    tree = to_tree(linked_ward,False)
    with open('newick.txt', 'w') as f:
        f.write(get_newick(tree, "", tree.dist, matrix.index))

    print('K-Means: {}'.format(grade(matrix.index, kmeans_result.labels_)))
    print('Ward Agglomerative: {}'.format(grade(matrix.index, agglomerative_ward.labels_)))
    print('Complete Link Agglomerative: {}'.format(grade(matrix.index, agglomerative_complete.labels_)))
    print('Single Link Agglomerative: {}'.format(grade(matrix.index, agglomerative_single.labels_)))
    print('Average Link Agglomerative: {}'.format(grade(matrix.index, agglomerative_average.labels_)))
    print('Random Clustering: {}'.format((random_ari_avg, random_tree_avg)))
