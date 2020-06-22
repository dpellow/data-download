# data-download

### Download bacterial references and PLSDB database
`scripts/download_script.sh` - script to download NCBI bacteria and Archaea references. Warning: This database is large.

`scripts/download_plsdb.sh` - script to download and extract the PLSDB plasmid sequences

each script should be run in the directory where you would like to download the files

### Split bacterial reference database into genomes and plasmids
`scripts/filter_plasmids_from_genomes.py` - script to create plasmid and genome fastas given single fasta input file

Usage: `python filter_plasmids_from_genomes.py -i <input fasta> -p <output plasmid fasta> -f <output genome fasta> [-mn <min length for plasmid (1000)] [-mx <max length for plasmid (1000000)]`

### Deduplicate sequences
`scripts/dedup.py` - script to remove exact duplicates in a fasta file. e.g. concatenate together the PLSDB fasta file and the plasmids split from refseq into one file and then deduplicate.

Usage: `python dedup.py <input fasta> <output fasta>`
