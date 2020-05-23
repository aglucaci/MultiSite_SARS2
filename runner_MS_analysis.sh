#!/bin/bash

Date="2020-05-11"
mkdir -p analysis
mkdir -p analysis/csvs

# ==================================================================================================================================
# Step 1
# python MS_Analysis_mod.py {Fasta} {List of Sites} > {Output CSV}
# ==================================================================================================================================

mkdir -p "analysis/csvs/"$Date

python3 MS_Analysis_mod.py data/sequences.ORF3a.compressed.fas 42,43,57,68,99,125,131,240 > "analysis/csvs/"$Date"/ORF3a_multisite_analysis.csv"

#python MS_Analysis_mod.py data/sequences.M.compressed.fas 30,69,109,132,141,143 > analysis/csvs/M_multisite_analysis.csv

#python MS_Analysis_mod.py data/sequences.N.compressed.fas 13,20,24,55,67,108,119,139,144,151,173,207,208,210,218,253,291,305,318,360,377,393,397,417 > analysis/csvs/N_multisite_analysis.csv

#python MS_Analysis_mod.py data/sequences.ORF1a.compressed.fas  16,84,86,92,166,210,265,274,286,333,398,428,454,447,486,519,549,580,609,650,652,717,748,872,892,894,924,1100,1143,1158,1160,1168,1202,1208,1250,1330,1352,1415,1640,1822,1840,1921,2062,2067,2098,2124,2144,2153,2242,2249,2391,2405,2470,2497,2500,2557,2575,2635,2796,2839,2842,3027,3058,3070,3071,3072,3076,3090,3227,3278,3308,3323,3353,3357,3447,3483,3512,3542,3580,3603,3606,3639,3644,3714,3725,3755,3757,3777,3856,3858,3870,3884,3899,3958,3983,4023,4097,4177,4220,4379,4381,4389 > analysis/csvs/ORF1a_multisite_analysis.csv

#python MS_Analysis_mod.py data/sequences.ORF7a.compressed.fas 70,92,121 > analysis/csvs/ORF7a_multisite_analysis.csv

#python MS_Analysis_mod.py data/sequences.ORF8.compressed.fas 8,84,121 > analysis/csvs/ORF8_multisite_analysis.csv

#python MS_Analysis_mod.py data/sequences.S.compressed.fas 29,61,138,231,294,598,614,620,623,675,723,731,824,934,936,1044,1100,> analysis/csvs/S_multisite_analysis.csv

#python MS_Analysis_mod.py data/sequences.ORF6.compressed.fas  > analysis/csvs/ORF6_multisite_analysis.csv

# ==================================================================================================================================
# Step 2
# python plot_jupyter_mod.py {CSV} {Gene} {FigureWidth} {FigureHeight} {Date}
# Outputs images to analysis/images
# Will also output a "value_counts" csv to analysis/csvs/Date
# ==================================================================================================================================

mkdir -p "analysis/images"
mkdir -p "analysis/images/"$Date

python3 plot_jupyter_mod.py "analysis/csvs/"$Date"/ORF3a_multisite_analysis.csv" ORF3a 50 20 $Date

# plot_jupyter_mod.py analysis/csvs/M_multisite_analysis.csv M 50 20

#python plot_jupyter_mod.py analysis/csvs/N_multisite_analysis.csv N 50 20

#python plot_jupyter_mod.py analysis/csvs/ORF1a_multisite_analysis.csv ORF1a 50 120

#python plot_jupyter_mod.py analysis/csvs/ORF7a_multisite_analysis.csv ORF7a 50 20

#python plot_jupyter_mod.py analysis/csvs/ORF8_multisite_analysis.csv ORF8 50 20

#python plot_jupyter_mod.py analysis/csvs/S_multisite_analysis.csv S 50 20

# ==================================================================================================================================
# End of file
# ==================================================================================================================================
