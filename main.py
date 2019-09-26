tr = TrueTree().load_true_tree('FundamentalsProgramming/trueTree.phy')
dm = CNVData().readCNVMatrix('FundamentalsProgramming/LS_blastn_Gar_noDenom.txt')
cl,rn = Cluster().cluster(dm,'ward')