import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from glob import glob

st.set_page_config(
    page_title="Filter Visualisation",
    page_icon="	:rainbow:",
    layout="wide",
    initial_sidebar_state="expanded",    
)

st.sidebar.header('Plotting Parameters')

def fillflag():
    filltrue = st.sidebar.checkbox('Fill Under Curve?')
    return filltrue
####
filltrue = fillflag()

#######
plt.rcParams['axes.labelsize']=40
plt.rcParams['axes.titlesize']=40
plt.rcParams['xtick.labelsize']=30
plt.rcParams['ytick.labelsize']=30
plt.rcParams['axes.linewidth']=2 # axes width]
plt.rcParams['lines.linewidth']=2 # axes width]

plt.rcParams['xtick.major.size']=12 # ticks]
plt.rcParams['xtick.major.width']=2 # ticks]
plt.rcParams['xtick.minor.size']=6 # ticks]
plt.rcParams['xtick.minor.width']=0.5 # ticks]
plt.rcParams['ytick.major.size']=12 # ticks]
plt.rcParams['ytick.major.width']=2 # ticks]
plt.rcParams['ytick.minor.size']=6 # ticks]
plt.rcParams['ytick.minor.width']=0.5 # ticks]
plt.rcParams['xtick.major.pad']=5 # prevent label overlap]
plt.rcParams['ytick.major.pad']=5 # prevent label overlap]
plt.rcParams['xtick.top']=True
plt.rcParams['ytick.right']=True
plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'

plt.rcParams['ytick.minor.visible']=True
plt.rcParams['xtick.minor.visible']=True

plt.rcParams['font.size']=30
plt.rcParams['font.family']='serif'
plt.rcParams['savefig.dpi']=200

plt.rcParams['legend.frameon']=False
plt.rcParams['legend.fancybox']=False
plt.rcParams['legend.fontsize']=40
plt.rcParams['legend.handlelength']=2

plt.rcParams['axes.axisbelow']=False
plt.rcParams['axes.facecolor']='white'
plt.rcParams['savefig.facecolor']='white'
#######

filters = glob('./observatories/**/*.dat',recursive=True)

fdict = {}
for f in filters:
    tmp = np.genfromtxt(f)
    name = f.split('/')[-1].split('.')[0]
    fdict[name] = tmp

options = st.multiselect(
    'What are your favourite filters?',
    list(fdict.keys()),
    ['Gaia_G'])

f = plt.figure(figsize=(18,9))
ax = f.add_subplot(111)

if len(options)>0:
    for pick in options:
        ax.plot(fdict[pick][:,0],fdict[pick][:,1],label=pick)
        if filltrue:
            ax.fill_between(fdict[pick][:,0],fdict[pick][:,1],alpha=0.3)
    ax.legend(fontsize='x-small',frameon=True)

ax.set_ylim(0.,1.1)
ax.set_xlabel('wavelength [nm]')
ax.set_ylabel('Transmission [%]')

st.pyplot(f,use_container_width=True)