#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:50:01 2020

@author: Alexander G Lucaci
"""
# =============================================================================
# Imports
# =============================================================================
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import sys


# =============================================================================
# Declares
# =============================================================================
# GISAID pulldown 05-11-2020
# Codon aware aligned

FASTA = sys.argv[1]
#print("# Processing:", FASTA)


Mutations = sys.argv[2]
Mutations = Mutations.split(",")

#print("# Will report on the following sites:", Mutations )


"""
#Mutations dict
Mutations = {}
Mutations[42] = ""
Mutations[43] = ""
Mutations[57] = ""
Mutations[68] = ""
Mutations[99] = ""
Mutations[125] = ""
Mutations[131] = ""
Mutations[240] = ""
Mutations[57] = {"CAG": "CAT", "CAC": "CAG"}
"""

print()
print(",".join(["Sequence ID", "Code"]))
datalist = {}


#sys.exit(1)
# =============================================================================
# Helper funct
# =============================================================================
#scan over sites, codon fashion.
#code for this sequence = ""
#does the site number, match a key in dictionary?
#if so, what is the codon?
def codons(s,frame=0):
    codons=[]
    end=len(s[frame:]) - (len(s[frame:]) % 3) - 1
    for i in range(frame,end,3):
        codons.append(s[i:i+3])
    return codons
# end method


# =============================================================================
# Main subroutine
# =============================================================================
with open(FASTA) as handle:
    for n, record in enumerate(SeqIO.parse(handle, "fasta")): 
        ID = record.id
        SEQ = record.seq
        
        #print(ID)
        start = 0
        #print("Num of NTs:", len(SEQ))
        #print("Num of Codons:", len(SEQ) / 3.0)
        
        code = []
        for i, codon in enumerate(codons(SEQ)):
            #print(i+1, codon)
            if str(i+1) in Mutations:
                #print(i+1, "Code", codon)
                code += [str(i+1)+str(codon)]
            #end if
        #end for
        
        #Save to CSV
        #python MS_Analysis.py > TEST.csv
        print(ID + ", ", " ".join(code))
        
        
        
        #datalist[ID] = "\t ".join(code)
        datalist[ID] = code
        #if n == 1: break
    #end for
#end with

    
# =============================================================================
# End of file
# =============================================================================
