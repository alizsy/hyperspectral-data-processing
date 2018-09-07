
# coding: utf-8

# In[ ]:


from spectral import *
import spectral.io.envi as envi
import matplotlib
import scipy.io as sci
import numpy as np
from tkinter import *
import tkinter.filedialog
import os

fnbsq=[]
n=-1
m=0
fnhdr = tkinter.filedialog.askopenfilenames(filetypes=[("header file","*.hdr")])
fns=master.tk.splitlist(fnhdr)
for i in fnhdr:
    bn = i.replace("hdr","bsq")
    img = envi.open(i,bn)
    arr = img.load()
    dims = np.shape(arr)
    nr = dims[0]-2
    nl = dims[1]-2
    nb = dims[2]
    o=-1
    del test
    test=np.zeros((nr*nl,nb))
    for j in range(1,nr):
        for k in range(1,nl):
            o=o+1
            test[o,:]=img.read_pixel(j,k)
            
    if m ==0:
        savepath =tkinter.filedialog.askdirectory()+'/'
    m=1
    savename =savepath+i.split("/")[-1].replace("hdr","txt")
    np.savetxt(savename,test)
    

