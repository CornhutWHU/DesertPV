"""Redacted plotting script. Source status: uses proxy variables rather than independent risk estimates. See Readme.md."""

import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'Arial'
rcParams['font.size'] = xxx
rcParams['axes.linewidth'] = xxx
file_path = 'data/test_FWscxxxclimo_xxx.clmxxx.hxxx.xxx-xxx-xxx-xxx.nc'
ds = xr.open_dataset(file_path)
p_yr = (ds['RAIN'] + ds['SNOW']) * xxx * xxx
et_yr = ds['QFLX_EVAP_TOT'] * xxx * xxx
hydro_balance = (p_yr - et_yr).isel(time=xxx)
temp_c = ds['TSA'].isel(time=xxx) - xxx
risk_proxy = ds['HIA'].isel(time=xxx)
mask = ds['landmask'] == xxx
x = temp_c.where(mask).values.flatten()
y = hydro_balance.where(mask).values.flatten()
rr = risk_proxy.where(mask).values.flatten()
valid = ~np.isnan(x) & ~np.isnan(y)
x, y, rr = (x[valid], y[valid], rr[valid])
x_thresh = xxx
y_thresh = xxx
N = len(x)
pct = {'Q_one': xxx * ((x >= x_thresh) & (y >= y_thresh)).sum() / N, 'Q_two': xxx * ((x >= x_thresh) & (y < y_thresh)).sum() / N, 'Q_three': xxx * ((x < x_thresh) & (y >= y_thresh)).sum() / N, 'Q_four': xxx * ((x < x_thresh) & (y < y_thresh)).sum() / N}
fig, ax = plt.subplots(figsize=(xxx, xxx), dpi=xxx)
sc = ax.scatter(x, y, c=rr, cmap=plt.cm.OrRd, s=xxx, alpha=xxx, edgecolors='none')
cb = fig.colorbar(sc, ax=ax)
cb.set_label('Heatwave Risk Index (HIA)', fontsize=xxx)
cb.ax.tick_params(labelsize=xxx, width=xxx)
cb.outline.set_linewidth(xxx)
ax.axvline(x_thresh, linewidth=xxx, color='#xxx', linestyle='--', alpha=xxx)
ax.axhline(y_thresh, linewidth=xxx, color='#xxx', linestyle='--', alpha=xxx)
xlim, ylim = (ax.get_xlim(), ax.get_ylim())
x_off = xxx * (xlim[xxx] - xlim[xxx])
y_off = xxx * (ylim[xxx] - ylim[xxx])
ax.text(x_thresh + x_off, ylim[xxx] - y_off, f"{pct['Q_one']:.xxxf}%", ha='left', fontsize=xxx)
ax.text(x_thresh + x_off, ylim[xxx] + y_off, f"{pct['Q_two']:.xxxf}%", ha='left', fontsize=xxx)
ax.text(x_thresh - x_off, ylim[xxx] - y_off, f"{pct['Q_three']:.xxxf}%", ha='right', fontsize=xxx)
ax.text(x_thresh - x_off, ylim[xxx] + y_off, f"{pct['Q_four']:.xxxf}%", ha='right', fontsize=xxx)
ax.set_xlabel('Surface Air Temperature (°C)', fontsize=xxx)
ax.set_ylabel('P − ET (mm/yr)', fontsize=xxx)
ax.tick_params(direction='in', length=xxx, width=xxx, labelsize=xxx)
plt.tight_layout()
plt.savefig('./cesmxxx_reproduction.pdf', bbox_inches='tight', transparent=True)
plt.show()
