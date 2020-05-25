#!/bin/bash

#input_csv_gene = "S_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF1a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "M_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "N_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF3a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF7a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF8_valuecounts_with_total_and_freqs.csv"


python plot_csvs.py S_valuecounts_with_total_and_freqs.csv
python plot_csvs.py ORF1a_valuecounts_with_total_and_freqs.csv
python plot_csvs.py M_valuecounts_with_total_and_freqs.csv
python plot_csvs.py N_valuecounts_with_total_and_freqs.csv
python plot_csvs.py ORF3a_valuecounts_with_total_and_freqs.csv
python plot_csvs.py ORF7a_valuecounts_with_total_and_freqs.csv
python plot_csvs.py ORF8_valuecounts_with_total_and_freqs.csv

cat clarifying_text.txt html/*_stackedbar.html > html/full.html
