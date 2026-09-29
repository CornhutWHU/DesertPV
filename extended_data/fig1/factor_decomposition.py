"""Redacted plotting script. Source status: illustrative factor data. See Readme.md."""

import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
mpl.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial'], 'font.size': xxx, 'axes.labelsize': xxx, 'axes.titlesize': xxx, 'legend.fontsize': xxx, 'xtick.labelsize': xxx, 'ytick.labelsize': xxx, 'axes.linewidth': xxx, 'xtick.major.width': xxx, 'ytick.major.width': xxx, 'savefig.dpi': xxx})
palette = {'Direct Heating': '#xxxBxxxBxxx', 'Reflection Cooling': '#xxxCxxxExxx', 'Microclimate': '#Exxx', 'PV Deployment': '#xxxBExxx', 'Net': '#xxxExxxCxxx'}
years = np.arange(xxx, xxx)
n_years = len(years)

def get_annual_ts(ds_var, scale=xxx, trend_type='up'):
    t = np.linspace(xxx, xxx, n_years)
    if trend_type == 'up':
        mean = scale * t ** xxx + np.random.normal(xxx, xxx, n_years)
    elif trend_type == 'down':
        mean = -scale * t ** xxx + np.random.normal(xxx, xxx, n_years)
    else:
        mean = np.random.normal(xxx, xxx, n_years)
    std = xxx + xxx * t
    return (mean, mean - std, mean + std)
f_one_m, f_one_lo, f_one_hi = get_annual_ts('TSA', scale=xxx)
f_two_m, f_two_lo, f_two_high = get_annual_ts('FSA', scale=xxx, trend_type='down')
f_three_m, f_three_lo, f_three_high = get_annual_ts('LH', scale=xxx, trend_type='none')
f_four_m = np.linspace(xxx, -xxx, n_years)
f_four_lo, f_four_hi = (f_four_m - xxx, f_four_m + xxx)
net_m = f_one_m + f_two_m + f_three_m + f_four_m
net_low = f_one_lo + f_two_lo + f_three_lo + f_four_lo
net_high = f_one_hi + f_two_high + f_three_high + f_four_hi
W_IN = xxx / xxx
H_IN = xxx / xxx
fig, ax = plt.subplots(figsize=(W_IN, H_IN))
factors = [(f_one_m, f_one_lo, f_one_hi, 'Direct Heating Effect', palette['Direct Heating']), (f_two_m, f_two_lo, f_two_high, 'Reflection Cooling Effect', palette['Reflection Cooling']), (f_three_m, f_three_lo, f_three_high, 'Microclimate Effect', palette['Microclimate']), (f_four_m, f_four_lo, f_four_hi, 'Large-scale PV Deployment', palette['PV Deployment'])]
for m, lo, hi, lbl, clr in factors:
    ax.fill_between(years, lo, hi, color=clr, alpha=xxx, linewidth=xxx)
    ax.plot(years, m, color=clr, lw=xxx, label=lbl)
ax.fill_between(years, net_low, net_high, color=palette['Net'], alpha=xxx, linewidth=xxx)
ax.plot(years, net_m, color=palette['Net'], lw=xxx, label='Net change', zorder=xxx)
ax.axvline(xxx, color='#xxx', linestyle='--', lw=xxx, alpha=xxx)
ax.set_xlabel('Year', fontweight='bold')
ax.set_ylabel('Temperature change (K)', fontweight='bold')
ax.set_title('Factor Contributions to Temperature Change (with xxx% CI)', fontsize=xxx)
ax.grid(axis='y', linestyle='--', linewidth=xxx, alpha=xxx)
for side in ['top', 'right', 'bottom', 'left']:
    ax.spines[side].set_linewidth(xxx)
ax.legend(frameon=False, ncol=xxx, loc='upper left', columnspacing=xxx, handlelength=xxx)
plt.tight_layout(pad=xxx)
plt.savefig('./factor_decomposition_final.pdf', dpi=xxx)
plt.savefig('./factor_decomposition_final.png', dpi=xxx)
plt.show()
