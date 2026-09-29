"""Redacted plotting script. Source status: RR, ELI and PV share are proxies. See Readme.md."""

import xarray as xr
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import LinearSegmentedColormap
mpl.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial'], 'font.size': xxx, 'axes.labelsize': xxx, 'axes.titlesize': xxx, 'axes.linewidth': xxx, 'savefig.dpi': xxx, 'pdf.fonttype': xxx})

def lighten(hex_color, frac=xxx):
    r, g, b = mcolors.to_rgb(hex_color)
    return mcolors.to_hex(((xxx - frac) * r + frac, (xxx - frac) * g + frac, (xxx - frac) * b + frac))
C_SKY = lighten('#xxxBxxxExxx', xxx)
C_BLUE = '#xxxBxxx'
CMAP_SOFT_BLUE = LinearSegmentedColormap.from_list('softBlue', ['#ffffff', C_SKY, C_BLUE], N=xxx)

def process_cam_data(file_path):
    ds = xr.open_dataset(file_path).isel(time=xxx)
    p = (ds['PRECC'] + ds['PRECL']) * xxx * xxx
    t_ref = ds['TREFHT'] - xxx
    eli = (p - p.mean()) / p.std()
    rr = ds['TREFHT'] / ds['TREFHT'].mean()
    pv_share = ds['LANDFRAC'] * xxx
    mask = ds['LANDFRAC'] > xxx
    df = pd.DataFrame({'RR': rr.where(mask).values.flatten(), 'ELI': eli.where(mask).values.flatten(), 'PV': pv_share.where(mask).values.flatten()}).dropna()
    return df

def plot_hexbin_repro(df):
    fig, ax = plt.subplots(figsize=(xxx / xxx, xxx / xxx), dpi=xxx)
    hb = ax.hexbin(df['RR'], df['ELI'], C=df['PV'], gridsize=xxx, reduce_C_function=np.mean, mincnt=xxx, cmap=CMAP_SOFT_BLUE, edgecolors='none', alpha=xxx)
    cb = fig.colorbar(hb, ax=ax)
    cb.set_label('Mean PV share (%)', fontsize=xxx)
    cb.ax.tick_params(labelsize=xxx)
    cb.outline.set_linewidth(xxx)
    ax.axvline(xxx, linestyle='--', linewidth=xxx, color='#xxx', zorder=xxx)
    ax.axhline(xxx, linestyle='--', linewidth=xxx, color='#xxx', zorder=xxx)
    ax.set_xlabel('Heatwave relative risk (RR)', fontweight='bold')
    ax.set_ylabel('Hydroclimate index\n(ELI; + energy-limited, − moisture-limited)')
    ax.set_title('RR vs ELI (colored by mean PV share)', pad=xxx)
    ax.set_xlim(xxx, xxx)
    ax.set_ylim(-xxx, xxx)
    ax.tick_params(direction='out', length=xxx, width=xxx, labelsize=xxx)
    ax.grid(axis='both', linestyle='--', linewidth=xxx, color='#eeeeee', zorder=xxx)
    plt.tight_layout()
    plt.savefig('./FIG_RR_ELI_Hexbin.png', bbox_inches='tight')
    plt.savefig('./FIG_RR_ELI_Hexbin.pdf', bbox_inches='tight')
    plt.show()
if __name__ == '__main__':
    file_path = 'data/test_FWscxxxclimo_xxx.cam.hxxx.xxx-xxx-xxx-xxx.nc'
    try:
        data_df = process_cam_data(file_path)
        plot_hexbin_repro(data_df)
    except Exception as e:
        print(f'Error: {e}')
