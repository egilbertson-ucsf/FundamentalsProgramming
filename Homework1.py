import os,sys, math

def read_clusters(clusters):
    file = open(clusters)
    clustDict = {}
    cells = file.readline().replace('"','').strip('\n').split(',')
    for line in file.readlines():
        if line[0]:
            for i in range(len(line.split(','))-1):
                if i > 1:
                    if line.split(',')[i] in clustDict:
                        clustDict[cells[i]].append(line.split(',')[i])
                    else:
                        clustDict[cells[i]] = line.split(',')[i]
    return clustDict

def read_expression(exp):
        file = open(exp)
        expDict = {}
        cells = file.readline().replace('"','').strip('\n').split(',')
        for line in file.readlines():
            for i in range(len(line.split(','))-1):
                if i > 0:
                    expDict[cells[i]] = i
        return expDict

def calc_clust_avg(clustDict, expDict, clustNum):
    for value in clustDict[clustNum]:
        
    return





def main():
    return
if __name__ == '__main__':
    cellClustDict = read_clusters(sys.argv[1])
    cellColDict = read_expression(sys.argv[2])
    main()
