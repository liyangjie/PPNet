#!/beegfs/home/lyj/miniconda3/envs/py3/bin/python
# -*- coding=utf-8 -*-
# @Author: Yangjie Li
import optparse
import os
import csv
import numpy as np
from scipy.stats import fisher_exact
from statsmodels.sandbox.stats.multicomp import multipletests
from method import methods
import sys
parse = optparse.OptionParser(usage='"usage:%prog [-n Number of annotation coloumns] [-m gene_presence_absence.csv] [-g GROUP_INFORMATION] [-a {0-81}] "', version="%prog 1.0")
parse.add_option('-m', dest='MATRIX', action='store', type=str, help='Input gene presence and absence matrix')
parse.add_option('-g', dest='GROUP', action='store', type=str, help='Input the group information')
parse.add_option('-o', dest='OUTDIR', action='store', type=str, default='.', help='DIRECTORY TO PLACE OUTPUT FILES. (DEFAULT = .)')
parse.add_option('-n', dest='NUM', action='store', type=int, default=14, help='How many coloumns are annotation information. (DEFAULT=14)')
parse.add_option('-a', dest='Algorithm',action='store',type=int, default=0, help='Select the algorithm for calculating the correlation coefficient[1-81], or set 0 to use all algorithm. (DEFAULT=0)' )
#parse.add_option('-p', dest='Top percent',action= 'store',type='int',default=100,help='Save the top x percent of data.[1-100],(DEFAULT=100)')

options, args = parse.parse_args()
###### Set Output Dir ######
outdir = options.OUTDIR
if not os.path.exists(outdir):
    os.mkdir(outdir)
if not outdir.endswith('/'):
    outdir +='/'
def main():
    #step1:
    if options.GROUP is None:
        print('The following arguments are required: -g')
        sys.exit()
    elif options.MATRIX is None:
        print('The following arguments are required: -m')
        sys.exit()       

    elif options.Algorithm not in range(82):
        print('-a parameter must be between 0 and 81')
        sys.exit()
    group1,group2 = get_group_info(options.GROUP)
    matrix = get_pan_matrix(options.MATRIX,options.NUM)
    p_values = get_pvalue(matrix, group1, group2)
    save_p_result(matrix,p_values,outdir+'Statistical_test_result.csv')#Save the DFG result
    #step2:
    matrix1 = np.delete(matrix, 1, 1)
    trim_row = np.where(p_values[:, -1] < 0.05)[0] + 1
    matrix2 = matrix1[trim_row]
    header = np.array(np.array([matrix1[0]]))
    Diff_gene_matrix = np.r_[header, matrix2]
    np.savetxt(outdir+'filted_phylogenetic_profile.csv',Diff_gene_matrix,fmt='%s',delimiter=',')
    pan_dic = {}
    for line in matrix2:
        pan_dic[line[0]]  = line[1:].tolist()
    sample_len=len(matrix2[0])-1
    if options.Algorithm ==0:
        create_all_net(pan_dic,sample_len,outdir)

    else:
        method = eval('methods.method_%s'%options.Algorithm)
        outdata = create_net(pan_dic, method,sample_len)
        saveNetData(outdata,outdir+'Netwrok_result_method%s.csv'%options.Algorithm)# Save the network result
    print('Finished')


def get_group_info(group_file):
    with open(group_file,'r') as f:
        f_csv = csv.reader(f)
        header = next(f)
        group1 = []# positive
        group2 = []# negetive
        for line in f_csv:
            if line[1]=='1':
                group1.append(line[0])
            elif line[1]=='0':
                group2.append(line[0])
    return group1,group2

def get_index(list1,list2): #linst1
    strain_index=[]
    for i in list1:
        strain_index.append(list2.index(i))
    return strain_index
#read the "gene_presence_absence.csv" file and return a np.array

def get_pan_matrix(pan_result,id = 14):
    f = open(pan_result, 'r')
    f_csv = csv.reader(f)
    lines = [line for line in f_csv]
    matrix = np.array(lines, dtype=object)
    head = matrix[0]
    trimed_index = [0,2]+list(range(id,len(head)))
    matrix=matrix[:,trimed_index]
    return matrix
# Calculate p values
def get_pvalue(matrix,group1,group2):
    p_values=[]
    header=list(matrix[0])
    #["Number_pos_present_in","Number_neg_present_in","Number_pos_not_present_in","Number_neg_not_present_in","Naive_p","Bonferroni_p"]
    group1_len = len(group1)
    group2_len = len(group2)
    group1_index = get_index(group1,header)
    group2_index = get_index(group2,header)
    for row in matrix[1:]:
        gene_name = row[0]
        array_1 = row[group1_index]
        array_2 = row[group2_index]
        gene_present_in_group1 = len(array_1[array_1!=''])
        gene_not_present_in_group1 = group1_len - gene_present_in_group1
        gene_present_in_group2 = len(array_2[array_2!=''])
        gene_not_present_in_group2 = group2_len - gene_present_in_group2
        p = fisher_exact([[gene_present_in_group1,gene_not_present_in_group1],
                          [gene_present_in_group2,gene_not_present_in_group2]],
                         alternative="greater")[1]
        p_values.append([gene_present_in_group1,gene_not_present_in_group1,
                        gene_present_in_group2,gene_not_present_in_group2,p])
    p_values=np.array(p_values)
    p_adj = multipletests(p_values[:,4],method='fdr_bh',alpha=0.05)[1]
    outdata = np.c_[p_values,p_adj]
    return outdata
def saveData(data,path):
    with open(path,'w',newline='') as out:
        out_csv = csv.writer(out)
        out_csv.writerows(data)

# Write the result of fisher's exact test
def save_p_result(matrix,p_result,SavePath):
    #edit the header info
    header = matrix[0]
    header_add =["Number_pos_present_in",
                 "Number_pos_not_present_in",
                 "Number_neg_present_in",
                 "Number_neg_not_present_in",
                 "Naive_p",
                 "Bonferroni_p"]
    header = list(header[[0,1]]) + header_add
    header = np.array([header])
    #format the output
    data =np.c_[matrix[1:,0:2],p_result]
    out_data = np.r_[header, data]
    saveData(out_data,SavePath)

def create_net(pan_dic,method,sample_len):
    outdata = []
    gene_list = list(pan_dic.keys())
    for index_A in range(len(gene_list)):
        geneA = gene_list[index_A]
        geneA_distribution = pan_dic[geneA]
        for index_B in range(index_A+1,len(gene_list)):
            geneB = gene_list[index_B]
            geneB_distribution = pan_dic[geneB]
            a = len([i for i in range(sample_len) if geneA_distribution[i] != '' and geneB_distribution[i] != ''])  # AandB
            b = len([i for i in range(sample_len) if (geneA_distribution[i] != '') and (geneB_distribution[i] == '')])  # AnotB
            c = len([i for i in range(sample_len) if (geneA_distribution[i] == '') and (geneB_distribution[i] != '')])  # BnotA
            d = len([i for i in range(sample_len) if (geneA_distribution[i] == '') and (geneB_distribution[i] == '')])  # nAnB
            try:
                s= method(a,b,c,d)
            except:
                print()
                s=0

            outdata.append([geneA,geneB,s])
    return outdata


def create_all_net(pan_dic,sample_len,outdir):
    names = locals()
    for x in range(1,82):
        names['out_%s'%x] = open(outdir+'Netwrok_result_method%s.csv'%x, 'w')
        eval('out_%s'%x).write('GeneA,GeneB,Attribute\n')
    gene_list = list(pan_dic.keys())
    for index_A in range(len(gene_list)):
        geneA = gene_list[index_A]
        geneA_distribution = pan_dic[geneA]
        for index_B in range(index_A+1,len(gene_list)):
            geneB = gene_list[index_B]
            geneB_distribution = pan_dic[geneB]
            a = len(
                [i for i in range(sample_len) if geneA_distribution[i] != '' and geneB_distribution[i] != ''])  # AandB
            b = len([i for i in range(sample_len) if
                     (geneA_distribution[i] != '') and (geneB_distribution[i] == '')])  # AnotB
            c = len([i for i in range(sample_len) if
                     (geneA_distribution[i] == '') and (geneB_distribution[i] != '')])  # BnotA
            d = len([i for i in range(sample_len) if
                     (geneA_distribution[i] == '') and (geneB_distribution[i] == '')])  # nAnB
            for x in range(1,82):
                try:
                    s = eval('methods.method_%s'%x)(a,b,c,d)
                except:
                    print('methods.method_%s'%x,a,b,c,d)
                    s=0
                eval('out_%s'%x).write('%s,%s,%s\n'%(geneA,geneB,s))
    for x in range(1,82):
        eval('out_%s' % x).close()
def saveNetData(data,SavePath='Network.csv'):
    header = [['GeneA','GeneB','Attribute']]
    out_data= header + data
    saveData(out_data,SavePath)

if __name__ == '__main__':
    main()

