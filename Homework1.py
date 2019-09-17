import os,sys
def read_exp_file(file):
    file = open(file)
    data = {}
    cellCol = {}
    cells = file.readline().replace('"','').strip('\n').split(',')
    for line in file:
        (gene,exp) = line.split(',',1)
        data[gene] = exp.strip('\n').split(',')
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
                    print(line[cell] in clustCell)
                    if int(line[cell]) not in clustCell:
                        clustCell[int(line[cell])] = [cells[cell]]
                        print(clustCell[int(line[cell])])
                        print([cells[cell]])
                        print('added not in')
                    else:
                        clustCell[int(line[cell])].append(cells[cell])
                        print('added else')
    return clustCell

def main():
    return
if __name__ == '__main__':
    expData, cellCol = read_exp_file(sys.argv[1])
    clustCell = read_clust_file(sys.argv[2])
    print(clustCell)
    main()
