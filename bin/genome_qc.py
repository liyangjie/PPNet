#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author: Yangjie Li
import os
import shutil
import argparse
from kneed import KneeLocator
parser = argparse.ArgumentParser()
parser.add_argument('input_genomes', help='[Required] The path of input sequences')

parser.add_argument('-o', '--output_dir', default='./PPNet_output',
                    help='The path of output (Default "./PPNet_output")')
parser.add_argument('-x', '--extend', default='fasta', help='The suffix of input data (Default "fasta")')
parser.add_argument('-c', '--cpus', help='number of CPUs to use', type=int, default=1)

args = parser.parse_args()


def main():
    input_path = args.input_genomes
    if not input_path.endswith('/'):
        input_path += '/'
    outdir = args.output_dir  # outputdir
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    if not outdir.endswith('/'):
        outdir += '/'
    ANIdir = outdir + 'ANI_output/'  # The path of pyani output file
    NR_dir = outdir + 'NR_data/'  # The path of NR data
    os.makedirs(NR_dir)
    file_extend = args.extend  # -x
    thread = args.cpus

    # Step1 : qualit check

    fasta_list = [f for f in os.listdir(input_path) if f.endswith(file_extend)]
    HQ_dir = outdir + 'HQ_data/'
    os.makedirs(HQ_dir)
    with open(outdir + 'Genome_N50s.tab', 'w') as out:
        for fasta in fasta_list:
            N50 = calcuN50(input_path + fasta)
            out.write('%s\t%s\n' % (fasta, N50))
            if N50 > 10000:
                os.system('cp %s %s' % (input_path + fasta, HQ_dir + fasta))

    os.system('average_nucleotide_identity.py -i %s -o %s -m ANIm --workers %s' % (HQ_dir, ANIdir, thread))

    N50_file = open(outdir + 'Genome_N50s.tab', 'r')
    N50_info = {}
    for line in N50_file:
        line = line.strip().split('\t')
        key = line[0].split('.')[0]
        N50_info[key] = int(line[1])
    N50_file.close()

    # 读取ANI
    ANI_file = open(ANIdir + 'ANIm_percentage_identity.tab', 'r')

    headline = ANI_file.readline().strip()
    ori_Strain_list = headline.split('\t')
    ANI_matrix = [line.split('\t')[1:] for line in ANI_file]
    ANI_file.close()
    # 读取ANC
    ANC_file = open(ANIdir + 'ANIm_alignment_coverage.tab', 'r')
    ANC_file.readline()
    ANC_matrix = [line.split('\t')[1:] for line in ANC_file]
    ANC_file.close()
    
    #寻找ANI和ANC的阈值
    ani_threshold_range = [1 - x / 10000 for x in range(21)] #[1-0.9980]
    
    #测试ANI阈值
    cluster_dic_nr_sizes=[]
    for ani_Threshold in ani_threshold_range:
        cluster_dic = []
        for row in range(len(ori_Strain_list)):
            Strain_A = ori_Strain_list[row]
            N50_A = N50_info[Strain_A]
            clust = [Strain_A]
            # for col in range(row+1,len(ori_Strain_list)): #取上三角
            for col in range(row):  # 取下三角
                Strain_B = ori_Strain_list[col]
                N50_B = N50_info[Strain_B]
                ANI = float(ANI_matrix[row][col])
                ANC1 = abs(1 - float(ANC_matrix[row][col]))
                ANC2 = abs(1 - float(ANC_matrix[col][row]))
                if ANI >= ani_Threshold:
                    clust.append(Strain_B)
            cluster_dic.append(clust)
        cluster_dic_nr = iter_clean(cluster_dic)
        cluster_dic_nr_size= len(cluster_dic_nr)
        cluster_dic_nr_sizes.append(cluster_dic_nr_size)
    knee_ani = KneeLocator(range(21),cluster_dic_nr_sizes,S=1,curve='convex',direction='decreasing',online=True).knee
    ani_Threshold = ani_threshold_range[knee_ani]
    #测试ANC阈值
    anc_threshold_range = [x/1000 for x in range(31)]
    cluster_dic_nr_sizes=[]
    for anc_Threshold in anc_threshold_range:
        cluster_dic = []
        for row in range(len(ori_Strain_list)):
            Strain_A = ori_Strain_list[row]
            N50_A = N50_info[Strain_A]
            clust = [Strain_A]
            # for col in range(row+1,len(ori_Strain_list)): #取上三角
            for col in range(row):  # 取下三角
                Strain_B = ori_Strain_list[col]
                N50_B = N50_info[Strain_B]
                ANI = float(ANI_matrix[row][col])
                ANC1 = abs(1 - float(ANC_matrix[row][col]))
                ANC2 = abs(1 - float(ANC_matrix[col][row]))
                if ANI >= ani_Threshold and ANC1 < anc_Threshold and ANC2 < anc_Threshold:
                    clust.append(Strain_B)
            cluster_dic.append(clust)
        cluster_dic_nr = iter_clean(cluster_dic)
        cluster_dic_nr_size= len(cluster_dic_nr)
        cluster_dic_nr_sizes.append(cluster_dic_nr_size)
    knee_anc = KneeLocator(range(31),cluster_dic_nr_sizes,S=1,curve='convex',direction='decreasing',online=True).knee
    anc_Threshold = anc_threshold_range[knee_anc]



    cluster_dic = []
    for row in range(len(ori_Strain_list)):
        Strain_A = ori_Strain_list[row]
        N50_A = N50_info[Strain_A]
        clust = [Strain_A]
        # for col in range(row+1,len(ori_Strain_list)): #取上三角
        for col in range(row):  # 取下三角
            Strain_B = ori_Strain_list[col]
            N50_B = N50_info[Strain_B]
            ANI = float(ANI_matrix[row][col])
            ANC1 = abs(1 - float(ANC_matrix[row][col]))
            ANC2 = abs(1 - float(ANC_matrix[col][row]))
            if ANI >= ani_Threshold and ANC1 < anc_Threshold and ANC2 < anc_Threshold:
                clust.append(Strain_B)
        cluster_dic.append(clust)
    cluster_dic_nr = iter_clean(cluster_dic)

    # 选取N50最大的基因组做为参考基因组
    out_file = open(outdir + 'cluster_result.tab', 'w')
    ref_Strain_list = []
    for group in cluster_dic_nr:
        if len(group) == 1:
            ref_strain = group[0]
        else:
            strain_N50s = [N50_info[s] for s in group]
            ref_id = strain_N50s.index(max(strain_N50s))  # 取最N50最大的基因组作为参考基因组
            ref_strain = group[ref_id]
        ref_Strain_list.append(ref_strain)
        out_line = ref_strain + '\t' + '\t'.join(group)
        out_file.write(out_line + '\n')
    # 将参考基因组数据都放到一个新的文件夹
    for f in ref_Strain_list:
        shutil.copy(HQ_dir + '%s.%s' % (f, file_extend), NR_dir)


def calcuN50(fasta, percent=50):
    BaseSum, Length = 0, []
    ValueSum, N50 = 0, 0
    from Bio import SeqIO
    for record in SeqIO.parse(open(fasta), "fasta"):
        BaseSum += len(record.seq)
        Length.append(len(record.seq))
    Length.sort(key=lambda x: -x)
    N50_pos = BaseSum / 100. * percent
    for value in Length:
        ValueSum += value
        if N50_pos <= ValueSum:
            N50 = value
            return N50


def nr(d, l1):  # 判断l1-[] 是否与d-[[]] 中的元素有交集，有返回True和index，没有返回True
    for i in range(len(d)):
        if len(set(l1) & set(d[i])) > 0:
            return True, i
    return False, None


def clean(d):  # 消除重复
    d2 = []
    for l1 in d:
        if nr(d2, l1)[0] == True:
            i = nr(d2, l1)[1]
            d2[i] = list(set(l1) | set(d2[i]))
        else:
            d2.append(l1)
    return d2


def iter_clean(d):  # 彻底消除重复
    n1 = len(d)
    d = clean(d)
    n2 = len(d)
    if n1 == n2:
        return (d)
    else:
        return iter_clean(d)


if __name__ == '__main__':
    main()

