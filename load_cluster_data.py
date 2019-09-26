import pandas as pd


def load_data(filename, index_dictionary=None):
    # load and transpose data
    df = pd.read_csv(filename, sep='\t', index_col=0).transpose()

    # drop "Total" row
    df = df.drop(['Total'])

    # normalize data
    df = (df - df.min()) / (df.max() - df.min())

    # fix labels
    df.index = fix_labels(df.index, index_dictionary)

    # replace NaN values and return
    return df.fillna(0)


def fix_labels(labels, index_dictionary):
    fixed_labels = []

    for label in labels:
        if label in index_dictionary:
            fixed_labels.append(index_dictionary[label])
        else:
            fixed_labels.append(label)

    return fixed_labels


if __name__ == '__main__':
    # Configuration Values
    filename = '..\LS_blastn_Gar_noDenom.txt'
    label_replace_dictionary = {
        'SM11_centroids_nucleotides': 'SnappingTurtle',
        'SM12_centroids_nucleotides': 'AnolisAgrei',
        'SM13_centroids_nucleotides': 'CaliforniaAlligatorLizard',
        'SM14_centroids_nucleotides': 'AfricanHouseSnake',
        'SM15_centroids_nucleotides': 'Cottonmouth',
        'SM16_centroids_nucleotides': 'SunbeamSnake',
        'SM17_centroids_nucleotides': 'AlligatorMiss',
        'SM18_centroids_nucleotides': 'FenceLizard',
        'SM19_centroids_nucleotides': 'BeardedDragon',
        'SM110_centroids_nucleotides': 'StinkpotTurtle',
        'SM111_centroids_nucleotides': 'SideneckTurtle',
        'SM112_centroids_nucleotides': 'GroundSkink',
        'SM113_centroids_nucleotides': 'CommonBoxTurtle',
        'SM114_centroids_nucleotides': 'ViperBoa',
        'SM115_centroids_nucleotides': 'LepardGecko',
    }

    # Routine
    matrix = load_data(filename, index_dictionary=label_replace_dictionary)
    print(matrix)
