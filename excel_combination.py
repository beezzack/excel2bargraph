# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, isdir, join
from glob import glob
import openpyxl
from time import gmtime, strftime


# %%
path = "./INPUT/"

files = listdir(path)


# %%
Col = ['Sample', 'Analyte', 'Most Freq.\r\nSize (nm)', 'Mean Size\r\n(nm)', 'No. of\r\nPeaks', 'Mean Inten.\r\n(counts)', 'Part. Conc.\r\n(parts/mL)', 'Diss. Inten.\r\n(counts)', 'Diss. Conc.\r\n(ppb)']


# %%
resultdf = pd.DataFrame(columns=Col)


# %%
for f in files:
    fullpath = join(path, f)

    if isfile(fullpath):
        data = pd.read_excel(fullpath, sheet_name='Sample Information',usecols=Col)

        resultdf = pd.concat([resultdf,data],axis=0,ignore_index=True)
        
    else:
        print("This is not a file : ", f)


# %%
resultdf.to_excel("./OUTPUT/mergeresult"+strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".xlsx",sheet_name='Sample Informations')

