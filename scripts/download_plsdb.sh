#! /bin/bash

BLAST_DIR=/specific/netapp5/gaga/dpellow/bin/ncbi-blast-2.9.0+/bin

if [ ! -d "plsdb" ]; then
  mkdir "plsdb"
fi

wget -O plsdb/plsdb_download.zip https://ccb-microbe.cs.uni-saarland.de/plsdb/plasmids/download/?zip
unzip plsdb/plsdb_download.zip -d plsdb
$BLAST_DIR/blastdbcmd -entry all -db plsdb/plsdb.fna -out plsdb/plasmids.fasta
rm plsdb/plsdb*
