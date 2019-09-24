import pandas as pd
import numpy as np

CNVDataFilePath = '...'


genomeReplaceDict = {
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