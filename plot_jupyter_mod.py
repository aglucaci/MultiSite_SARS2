#!/usr/bin/env python
# coding: utf-8

# =============================================================================
# Imports
# =============================================================================

import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import sys

from matplotlib.pyplot import figure


# =============================================================================
# Declares
# =============================================================================
datafile = sys.argv[1]
gene = sys.argv[2]
figsize_width = int(sys.argv[3])
figsize_height = int(sys.argv[4])
Date = sys.argv[5]

# =============================================================================
# Main
# =============================================================================
print("# Processing:", datafile)

data = pd.read_csv(datafile)

#print("COLUMNS:", data.columns.tolist())

fig, ax = plt.subplots()

#plt.figure(figsize=(20,110)) 

data['Code'].value_counts().plot(ax=ax, kind='barh', figsize=(figsize_width, figsize_height), fontsize=12, title=gene + " MULTISITE ANALYSIS")

# The code is a concat'd string of SITE# and codon at that position
# site 42, codon CCT
# site 32, codon TTC , etc,
# This is only done for interesting sites
fig.savefig("analysis/images/"+Date+"/"+gene+".png")

# Pie
fig, ax = plt.subplots()
#plt.figure(figsize=(20,110)) 
data['Code'].value_counts().plot(ax=ax, kind='pie', figsize=(figsize_width, figsize_height), fontsize=12, title=gene + " MULTISITE ANALYSIS")
fig.savefig("analysis/images/"+Date+"/"+gene+"_pie.png")


# =============================================================================
# Saving to file, csv
# =============================================================================

df = data

df2 = df["Code"].value_counts()
df2.to_csv("analysis/csvs/"+Date+"/"+gene+"_valuecounts.csv")

#df['count'] = df.groupby('group')['group'].transform('count')

#df["Counts"] = df[" Code"].value_counts()
#df[" Code"].value_counts().rename_axis('created_at').reset_index(name='count')

#print(df)

#datafile = datafile.replace(".csv", "")
#df.to_csv(datafile+"_withvaluecounts.csv")
# =============================================================================
# 
# =============================================================================
