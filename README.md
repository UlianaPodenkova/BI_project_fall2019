# BI_project_fall2019
# Phylogenetic analysis as a forensic tool

## Tasks of the project
1. Review and compare existing approaches to convert NGS sequence variants into haplotypes
2. Identify common problems in these approaches 

## Methods
* Step 1 - Choose the options to run CoalEvol, which allows simulating coalescence evolution. Created 6 datasets (varied parameters: mutation rate and Ne-effective population size).
All parameters may be found in the CoalEvol Manual

Example:

```'/home/uliana/Загрузки/CoalEvol-7.3.5/exe/CoalEvol7.3.5_Linux' -n10 -s5 1139 -e1000 2 -f4 0.3 0.1 0.2 0.2 -u0.001 -xseqGMRCA -bseqs```

* Step 2 - Reads stimulation using ART Illumina (ART is a set of simulation tools that takes a set of DNA sequences and generate synthetic next-generation sequencing reads).

We simulated error-free 150 bp paired-end reads with a read count of 100 reads, mean size of 215 bp for DNA fragments, and a standard deviation of 120 bp for DNA fragment size.

```'/home/uliana/Загрузки/art_bin_MountRainier/art_illumina' -ss MSv1 -i ./seqsample1.fa -o ./paired_end_com -ef -l 150 -c 100  -p -m 215 -s 120 -sam```

* Step 3 - Using Bowtie2. 

``` samtools view -b seq1.sam > seq1.bam
samtools sort seq1.bam -o seq1.sorted -O BAM
samtools index seq1.sorted
samtools bam2fq seq1.sorted | seqtk seq -A - > output.fa
```

* Step 4 - Choice of haplotype callers. The haplotype programs also varied greatly in terms of their ease-of-use. This variation is due to differences in coding language, program dependencies, availability of executable files, absence of comprehensive documentation and lack of example datasets.
Based on this, the following were selected:2SNV, CliqueSNV, SAVAGE.

    Run 2SNV

``` ~/haplotypers/2snv$ java -jar 2snv-1.0.jar output.fa 1000 -t 30 -o haplotypes.fa```

   Run CliqueSNV
   
``` ~/haplotypers/CliqueSNV$ java -jar clique-snv.jar -m snv-illumina -in seqres1.sam -outDir snv_output1/```

SAVAGE - the assembled haplotypes were shorter than actual length of ground truth haplotypes so I did not compare it with other programs.

* Step 5 - Analysis and comparison. 

*UniFrac distance*

*Edit distance*

*Precision*

*Recall*

Simulated data can be represented as P = {(hi., pi.), i = 1, 2, …} – the ground truth haplotypes hi. and their associated abundances pi. (∑ pi. = 1), and Q = {(fi., qi.), i = 1, 2, …} – the set of predicted haplotypes fi together with their predicted abundances qi..We define precision as ![Альтернативный текст](https://www.biorxiv.org/sites/default/files/highwire/biorxiv/early/2019/11/01/828350/embed/inline-graphic-1.gif)  and recall as . 
![Альтернативный текст](https://www.biorxiv.org/sites/default/files/highwire/biorxiv/early/2019/11/01/828350/embed/inline-graphic-2.gif) define TP (true positive) and FP (false positive) differently for reference-based and de novo tools. We define FN (false negative) as 1 − TP, for both assembly strategies equally.(Eliseev A. et al., 2019). The UniFrac distance takes into account both the phylogenetic structure of the haplotype set and their frequency distribution, which makes it ideal for incorporating sensitivity to errors in frequency prediction (McClelland and Koslicki, 2018).
   
   CliqueSNV produced estimates close to the true number of haplotypes. We conclude that haplotype reconstruction from NGS short reads is unreliable due to high genetic diversity of viruses and the inability of programs to take into account recombination process.
