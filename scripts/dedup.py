# deduplicating exact duplicate sequences in fasta

import argparse,sys
from seq_utils import *

def parse_user_input():
    parser = argparse.ArgumentParser(
        description=
        'deduplicate sequences in a file'
    )
    parser.add_argument('-i','--infile',
     help='Input fasta file name',
     required=True, type=str
     )
    parser.add_argument('-o','--outfile',
     help='output fasta file name',
     required=True, type=str
     )

    return parser.parse_args()

def dedup(infile,outfile):

    seqs = []
    headers = []

    fp = open(infile)
    for name,seq,_ in readfq(fp):
        headers.append(name)
        seqs.append(seq)
    fp.close()

    seq_lens = [len(seq) for seq in seqs]
    removed_set = set()
    for i in range(len(seqs)):
      if i%100==0: print(i)
      targetlen = seq_lens[i]
      doubled_seq = seqs[i]+seqs[i]
      for j in range(i+1,len(seqs)):
        if j in removed_set: continue
        if targetlen == seq_lens[j]:
            query = seqs[j]
            r_query = query[::-1]
            comp = complement(query)
            rc = comp[::-1]
            if query in doubled_seq or r_query in doubled_seq or comp in doubled_seq or rc in doubled_seq:
                 print("{} is the same as {}".format(headers[i],headers[j]))
                 removed_set.add(j)

    print("{} duplicates removed".format(len(removed_set)))

    with open (outfile,'w+') as o:
      for i in range(len(seqs)):
        if i not in removed_set:
          o.write('>'+headers[i]+'\n')
          o.write(seqs[i]+'\n\n')


if __name__ == "__main__":

    args = parse_user_input()

    infile = args.infile
    outfile = args.outfile

    dedup(infile,outfile)
