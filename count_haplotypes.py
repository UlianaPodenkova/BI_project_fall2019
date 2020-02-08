#code from https://github.com/kmgibson/Viral-Intra-Host-Simulation-Generation

!/usr/bin/env python2

from Bio import SeqIO
from collections import Counter
import argparse

# run like:
# python count_haps.py -input [input_fasta_file] -output [output_file_name.fasta] > count_haps.txt
# you need a count_haps.txt file for each sequence directory in each replicate in each parameter directory

parser = argparse.ArgumentParser()
parser.add_argument("-input", help="input file")
parser.add_argument("-output", help="output file")
args = parser.parse_args()


counts = Counter()
for s in SeqIO.parse(args.input, "fasta"):
    counts[str(s.seq)] += 1

num = 1

with open(args.output, "w") as outh:
    seq = args.input.split(".")[0]
    for sequence, count in counts.most_common():
        print "%s\t%d" % (sequence, count)
        if count > 1:
            print >> outh, ">duplicate_from_args.input_%s" % seq, num
            print >> outh, "%s" % sequence
            num += 1
            
         
