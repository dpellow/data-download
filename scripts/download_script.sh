#! /bin/bash

if [ ! -d "bacteria" ]; then
  mkdir "bacteria"
fi

wget -O bacteria_summary.txt ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/assembly_summary.txt
awk -F '\t' '{if($12=="Complete Genome") print $20}' bacteria_summary.txt > bacteria_links.txt

for next in $(cat bacteria_links.txt); do 

   f=`echo $next | awk -F '/' ' { print $NF } ' `
   if [ ! -e bacteria/"$f"_genomic.fna  ] || [ ! -e bacteria/"$f"_genomic.fna.gz ]; then
      wget -P bacteria  -a download.log "$next"/"$f"_genomic.fna.gz;
#      echo "$next"/"$f"_genomic.fna.gz;
   fi
   

done

if [ ! -d "archaea" ]; then
  mkdir "archaea"
fi

wget -O archaea_summary.txt  ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/archaea/assembly_summary.txt
awk -F '\t' '{if($12=="Complete Genome") print $20}' archaea_summary.txt > archaea_links.txt

for next in $(cat archaea_links.txt); do

   f=`echo $next | awk -F '/' ' { print $NF } ' `
   if [ ! -e archaea/"$f"_genomic.fna  ] || [ ! -e archaea/"$f"_genomic.fna.gz ]; then
      wget -P archaea -a download.log "$next"/"$f"_genomic.fna.gz;
#      echo "$next"/"$f"_genomic.fna.gz;
   fi


done


gunzip bacteria/*.gz
gunzip archaea/*.gz

cat bacteria/*.fna > bacteria/all_bac.fasta
cat archaea/*.fna > archaea/all_archaea.fasta

