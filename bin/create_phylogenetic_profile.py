#! /usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author: Yangjie Li
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('input_genomes',help='[Required] The path of input sequences')

parser.add_argument('-o','--output_dir',default='./',help='The path of output (Default "./")')
parser.add_argument('-x','--extend',default ='fasta',help='The suffix of input data (Default "fasta")')
parser.add_argument('-c','--cpus',help = 'number of CPUs to use', type=int, default=1)

args = parser.parse_args()
    
input_path = args.input_genomes
if not input_path.endswith('/'):
    input_path+='/'

outdir = args.output_dir #outputdir
if not outdir.endswith('/'):
    outdir+='/'

file_extend = args.extend #-x
thread = args.cpus
#prokka 进行基因组注释
gff_out = outdir+'Gff_file/'
os.makedirs(gff_out)
fasta_list = [f for f in os.listdir(input_path) if f.endswith(file_extend)]
roary_result = outdir+'Roary_result'
def main():
    for f in fasta_list:# f= 'SS1021.fna'
        
        strain_name = f.split('.')[0]
        f = input_path+f
        prokka_result=outdir+'Prokka_result/%s'%strain_name
        os.system('prokka --kingdom Bacteria --locustag %s --cpus %s --prefix %s --outdir %s %s'%(strain_name,thread,strain_name,prokka_result,f))
        source_file = outdir+'Prokka_result/%s/%s.gff'%(strain_name,strain_name)
        os.system('cp %s %s'%(source_file,gff_out))
    

    #roary 构建pan基因组
    os.system('roary -p %s -f %s %s/*gff'%(thread,roary_result,gff_out))


if __name__ == '__main__':
    main()


