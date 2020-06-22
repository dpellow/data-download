# filter plasmid sequences from the genome references

import argparse,sys
from seq_utils import *

def parse_user_input():
    parser = argparse.ArgumentParser(
        description=
        'filter_plasmids_from_genomes creates fasta files of only plasmids and only genomes'
    )
    parser.add_argument('-i','--infile',
     help='Input fasta file',
     required=True, type=str
     )
    parser.add_argument('-p','--plasmids',
     help='output file name for the plasmids',
     required=True, type=str
     )
    parser.add_argument('-f','--filtered',
     help='output file name for the genomes with plasmids removed',
     required=True, type=str
     )
    parser.add_argument('-mn','--min_len',
     help='Minimum length for plasmid sequence to be saved',
     required=False, type=int
     )
    parser.add_argument('-mx','--max_len',
     help='Maximum length for sequence to be considered plasmid',
     required=False, type=int
     )

    return parser.parse_args()



def filter_plasmids(infile,filtered_file,plasmid_file,min_len=1000,max_len=1000000):
  plasmid_count = 0
  removed_count = 0
  chrom_count = 0
  fp = open(infile)
  with open(filtered_file,'w') as o1, open(plasmid_file,'w') as o2:
    for name,seq,_ in readfq(fp):
      if "plasmid" in name.lower():
        seq_len = len(seq)
        if seq_len < min_len or seq_len > max_len:
          removed_count += 1
          continue
        plasmid_count += 1
        o2.write(">"+name+'\n'+seq+"\n")
      else:
        chrom_count += 1
        o1.write(">"+name+'\n'+seq+"\n")

  fp.close()
  print("Plasmids: {}. Removed: {}. Chromosomes: {}".format(plasmid_count,removed_count,chrom_count))


if __name__ == "__main__":

    args = parse_user_input()

    infile = args.infile
    filtered_file = args.filtered
    plasmid_file = args.plasmids

    MIN_PLAS_LEN = 1000
    MAX_PLAS_LEN = 1000000
    if args.min_len:
        MIN_PLAS_LEN = args.min_len
    if args.max_len:
        MAX_PLAS_LEN = args.max_len

    filter_plasmids(infile,filtered_file,plasmid_file,MIN_PLAS_LEN,MAX_PLAS_LEN)
