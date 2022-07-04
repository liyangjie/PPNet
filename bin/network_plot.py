#!/usr/bin/env python
# -*- coding=utf-8 -*-
# @Author: Yangjie Li
from pyvis.network import Network
import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('Network_file',help='[Required] The path of input sequences')
parser.add_argument('-o','--output_dir',default='./',help='The path of output (Default "./")')
parser.add_argument('-pt','--percentage_threshold',default=1,help='What percentage of interactions will be visualized (Default "1")')


args = parser.parse_args()
input_file = args.Network_file
outdir = args.output_dir #outputdir

net = Network(height='100%', width='100%')
#got_net.barnes_hut()
got_data = pd.read_csv(input_file)
got_data =got_data.sort_values(by='Attribute',ascending= False) #order

size = len(got_data)
got_data = got_data[0:size//100]

sources = got_data['GeneA']
targets = got_data['GeneB']
weights = got_data['Attribute']

edge_data = zip(sources, targets, weights)


for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]
    net.add_node(src, src, title=src)
    net.add_node(dst, dst, title=dst)
    net.add_edge(src, dst, value=w)

net.options.edges.smooth.type='discrete'
net.show_buttons(filter_=['physics','nodes', 'edges',])
net.save_graph(outdir+'Gene_Net.html')
