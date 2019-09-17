import os,sys
def read_exp_file(file):
    file = open(file)
    data = {}
    cellCol = {}
    cells = file.readline().replace('"','').strip('\n').split(',')
    cells = cells[1:]
    for line in file:
        (gene,exp) = line.split(',',1)
        data[gene] = exp.replace('\n','').split(',')
        if len(data[gene]) != 121:
            print('adding length')
            data[gene].append('')
    for cell_i in range(len(cells)):
        cellCol[cells[cell_i]] = cell_i
    return data, cellCol

def read_clust_file(file):
    file = open(file)
    clustCell = {}
    cells = file.readline().replace('"','').strip('\n').split(',')
    for line in file.readlines():
        line = line.replace('"','').strip('\n').split(',')
        if line[0]=='TRUE':
            for cell in range(len(line)):
                if cell > 1:
                    if int(line[cell]) not in clustCell:
                        clustCell[int(line[cell])] = [cells[cell]]
                    else:
                        clustCell[int(line[cell])].append(cells[cell])
    return clustCell

def calc_avgs(clustNum, expData, cellCol, clustCell):
    geneAvgs =  {}
    for gene in expData.keys():
        sum = 0
        count = 0
        for cell in clustCell[clustNum]:
            if expData[gene][cellCol[cell]] != '':
                sum += float(expData[gene][cellCol[cell]])
                count += 1
        if count == 0:
            avg = 0
        else:
            avg = sum/count
        geneAvgs[gene] =  avg
    return geneAvgs

def main():
    return
if __name__ == '__main__':
    expData, cellCol = read_exp_file(sys.argv[1])
    clustCell = read_clust_file(sys.argv[2])
    clusterDicts = []
    for cluster in range(len(clustCell.keys())):
        clusterDicts.append(calc_avgs(cluster+1, expData, cellCol, clustCell))
    print(clusterDicts)
    main()
