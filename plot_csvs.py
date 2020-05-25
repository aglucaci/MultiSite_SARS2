#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports
import os
import pandas as pd
import plotly.graph_objects as go
import sys

# In[2]:


#Declares
DATADIR = "analysis/csvs"

#Get list of folders, which correspond to the date in the time series.
Dates = [x[0].replace(DATADIR+"/", "") for x in os.walk(DATADIR) if "Archive" not in x[0] and x[0] != DATADIR]
Dates.sort()
Dates.remove("2020-05-13") # had a processing error.

input_csv_gene = sys.argv[1]

#input_csv_gene = "S_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF1a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "M_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "N_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF3a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF7a_valuecounts_with_total_and_freqs.csv"
#input_csv_gene = "ORF8_valuecounts_with_total_and_freqs.csv"


gene = input_csv_gene.split("_")[0]


# In[3]:


#Dates


# In[4]:


# For the element, "Code", in May 30, get its values across all dates. 
# I need the "Set" of all codes
# So I have "Code"_1 and List_1 of all values across each date.
# x = Dates
# y = Frequency values of each "Code"
# and create a subplot for each one.

#Set of Codes.
# Open every "S_valuecounts_with_total_and_freqs.csv" and add to a list, return the set.

list_of_codes = []

for day in Dates:
    search_dir = DATADIR + "/" + day
    search_file = search_dir + "/" + input_csv_gene
    df = pd.read_csv(search_file)
    Codes = df["Code"]
    for item in Codes:
        list_of_codes += [item]
#end for


 


# In[5]:


elements = {}

for n, item in enumerate(set(list_of_codes)):
    print(n, item, "\n")
    elements[item] = {}


# In[ ]:


for item in elements.keys():
    print("Processing:", item)
    
    # For each element, 
    # Search each date.
    # Is the element present? If Yes, report the Freq. If no report 0
    # 
    for day in Dates:
        search_dir = DATADIR + "/" + day
        search_file = search_dir + "/" + input_csv_gene
        df = pd.read_csv(search_file)
        Codes = df["Code"]
        elements[item][day] = 0 # default value
        for n, seq_code in enumerate(Codes):
            if seq_code == item:
                elements[item][day] = df["Frequency"][n]
            #end if
        #end second inner for
    #end inner for
#end outer for

    
        


# In[ ]:


#elements


# In[ ]:


# Plotting
# Plot "Elements"
# Key1 is the Sequence "Code"
# Key2 is the Date
# Key3 is the codes frequency on that date.

Key1 = elements.keys()
Key2 = Dates


fig = go.Figure()

for seq_Code in elements.keys():
    #print("Processing:", seq_Code)
    list_of_Frequencies = []
    for day in Dates:
        list_of_Frequencies += [elements[seq_Code][day]]
    #end for
    #print(seq_Code, Dates, list_of_Frequencies)
    
    #print("Adding:", seq_Code, Dates, list_of_Frequencies)
    #print()
    fig.add_trace(go.Bar(x=Dates, y=list_of_Frequencies, name=seq_Code, text=seq_Code, marker={'color': y,
    'colorscale': 'Viridis'}))
    #x unified
    #hover_name="country", hover_data=["continent", "pop"]
#end for
    

#fig.add_trace(go.Scatter(x=list_of_Dates, y=list_of_Frequencies, name=seq_Code)


#fig.add_trace(go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
##                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
##                    ]))


# Edit the layout
fig.update_layout(title='SARS-CoV-2 (' + gene + ') Mutation Fingerprint - Timeseries Analysis (num_codes=' + len(elements.keys()) + ')',
                   xaxis_title='',
                   yaxis_title='Frequency',
                   width=1000, height=600)

#fig.update_layout(showlegend=False)

# Change the bar mode
fig.update_layout(barmode='stack')
fig.update_layout(legend_orientation="h")
#fig.update_layout(hovermode="x unified")
fig.update_layout(autosize=True)
fig.show()


import plotly.express as px

#fig =px.scatter(x=range(10), y=range(10))
os.system("mkdir -p html")
fig.write_html("html/" + input_csv_gene.replace(".csv","") + "_stackedbar.html")


# In[ ]:


#End of file

