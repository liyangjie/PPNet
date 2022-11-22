#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author: Yangjie Li
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i1','--input_genomes',help='[Required] The path of input genomes')
parser.add_argument('-i2','--phenotype',help='[Required] The path of phenotype (e.g., pathogenic or non-pathogenic) of all strains')
parser.add_argument('-o','--output_dir',default='./PPNet_output',help='The path of output (Default "./PPNet_output")')
parser.add_argument('-x','--extend',default ='fasta',help='The suffix of genomes data (Default "fasta")')
parser.add_argument('-c','--cpus',help = 'number of CPUs to use', type=int, default=1)
parser.add_argument('-a', '--Algorithm', help='[Required] Select the algorithm for calculating the correlation coefficient[1-81], or set 0 to use all algorithm.' )
parser.add_argument('-pt','--percentage_threshold',default=1,help='What percentage of interactions will be visualized (Default "1")')
parser.add_argument('-t1','--ANI_threshold',default = 'auto',
					help='The threshold of ANI  [0-0.9999], or set as "auto"  to select the inflection point as the threshold for ANI. (Default "auto")')
parser.add_argument('-t2','--ANC_threshold',default = 'auto',
					help='The threshold of |1-ANC| [0-0.9999], or set as "auto" to select the inflection point as the threshold for |1-ANC|. (Default "auto")')

args = parser.parse_args()

genomes = args.input_genomes

cpus = args.cpus
extend = args.extend

outdir = args.output_dir
if not os.path.exists(outdir):
    os.mkdir(outdir)
if not outdir.endswith('/'):
    outdir +='/'


print('Step1: genmoe check')
os.system('genome_qc.py -o %s -x %s -c %s %s'%(outdir,extend,cpus,genomes))


NR_data = outdir+'NR_data'

print('Step2: create_phylogenetic_profile')
os.system('create_phylogenetic_profile.py -o %s -x %s -c %s %s'%(outdir,extend,cpus,NR_data))


print('Step3: create network')
os.system('create_net.py -g %s -m %s/gene_presence_absence.csv -a %s -o %s'%(args.phenotype,outdir+'Roary_result',args.Algorithm,outdir))

print('Step4: Visualize the network')
if args.Algorithm == 0:
	for x in range(1,82):
		input4 = outdir+'Netwrok_result_method%s.csv'%x
		os.system('network_plot.py -o %s -pt %s %s'%(outdir,args.percentage_threshold,input4))

else:
	input4 = outdir+'Netwrok_result_method%s.csv'%args.Algorithm
	os.system('network_plot.py -o %s -pt %s %s'%(outdir,args.percentage_threshold,input4))
