# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import numpy as np
import pandas as pd
from os import listdir, makedirs
from os.path import isfile, isdir, join
import matplotlib.pyplot as plt
from time import gmtime, strftime


# %%
path = "./INPUT/"
files = listdir(path)
Col = ['Diameter (nm)', 'Frequency']


# %%
print(">>Hi!")
parameterTE = float(input(">>Enter your parameter(TE): "))
parameterSF = float(input(">>Enter your parameter(Sample flowrate): "))
time = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
makedirs('./OUTPUT/'+time+'/')
for f in files:
    fullpath = join(path, f)
    print(">>"+f)
    option = int(input(">>dilution factor 1: '1', 2: '10': "))
    while(option>2 or option<1):
        option = int(input(">>dilution factor 1: '1', 2: '10': "))
    if isfile(fullpath):
        data = pd.read_excel(fullpath, sheet_name='Size Histogram',usecols=Col)
        if(option == 1):
            data['Number Concentration (10^4 particles/L)'] = (data['Frequency'] / ((parameterTE / 100) * (parameterSF / 60) * 50)) / 10
        elif(option == 2):
            data['Number Concentration (10^4 particles/L)'] = (data['Frequency'] / ((parameterTE / 100) * (parameterSF / 60) * 50))

        ax = data.plot.bar(x='Diameter (nm)', y='Number Concentration (10^4 particles/L)', rot=0, xticks = np.arange(0, 200, step=50), yticks = np.arange(0, 1000, step=200), width = 1.0)
        ax.set_xlim(0, 200) 
        ax.set_ylim(0, 1000) 
        ax.set_ylabel("Number Concentration (10^4 particles/L)")
        ax.get_legend().remove()

        fig = ax.get_figure()
        fig.set_size_inches(8,6)
        fig.set_dpi(200)
        fig.savefig('./OUTPUT/'+time+'/'+f[:-5]+'.png')
        plt.close(fig)
        print("OK!")
        
    else:
        print("This is not a file : ", f)

while True:
    if not input("Done! Press Enter to end"):
        print("exiting program.")
        break

