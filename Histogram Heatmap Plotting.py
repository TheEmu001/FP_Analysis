# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:00:32 2020

@author: TGlaze
"""


### Libraries ###
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

 
### Bring in data, filter out any NaN values ###
""" 
Make sure to properly set both the path name and file name. 
"""
path_name = "C:/Users/AD-AnestNorrislab/Box/Norris Lab shared/Tera Data & Programs/FP Testing/FP 3.9.2020/F2/"
file_name = "VGlut-CreC228F2_avgFluor_testing_Test1_2020-03-09T14_04_43.csv"
# path_name = "C:/Users/HP/Desktop/Python Programs/"
# file_name = "centroid_data.csv"
data = pd.read_csv(path_name+file_name)
#print(data.size) # printing size to verify that NaNs are removed
bool_remove_nan_x = pd.notnull(data['X'])
data = data[bool_remove_nan_x]
#print(data.size)
bool_remove_nan_y = pd.notnull(data['Y'])
data = data[bool_remove_nan_y]
#print(data.size)


### Assign data to variables x and y ###
x, y = data["X"], data["Y"] #[0:2000]


### Scatter plot to visualize data ###
# Create a figure with 2 plot areas
fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(21, 5))
 
# Everything sarts with a Scatterplot
axes[0].set_title('Scatterplot')
axes[0].plot(x, y, 'ko')
 

### 2D Histogram ###
nbins = 150     # number of bins, adjustable
gmma = 0.3      # Gamma, changes the normalization for datapnts in 2D Histogram
                # Smaller values reveal the lighter tracks where less time was 
                # spent; see: 
# https://matplotlib.org/gallery/scales/power_norm.html#sphx-glr-gallery-scales-power-norm-py
axes[1].set_title('2D Histogram')
plt.xlabel("Distance, Pixels")

counts, xedges, yedges, im = axes[1].hist2d(x, y,
                bins=nbins, cmap=plt.cm.YlGnBu_r, norm=mcolors.PowerNorm(gmma))
                # hist2d gives multiple things; im needed for colorbar
cbar = plt.colorbar(im, ax = axes[1])
#cbar.mappable.set_clim(0,100) # comment this out to set cbar to auto range
# or chnage to alter the range of the colorbar
cbar.ax.set_yticklabels(['Never', '','','', 'Most Often'])
# Change labels above to alter labels on colorbar


### Save Figure ###
# Make sure to name it something identifyable
plt.savefig("Testing_2DHistogram.pdf")