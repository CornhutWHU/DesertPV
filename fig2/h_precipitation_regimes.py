"""Redacted plotting script. Source status: CESM input with simplified regime construction. See Readme.md."""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'Arial'
rcParams['font.size'] = xxx
rcParams['axes.linewidth'] = xxx
nc_file = 'data/test_FWscxxxclimo_xxx.cam.hxxx.xxx-xxx-xxx-xxx.nc'
ds = xr.open_dataset(nc_file)
p_day = (ds['PRECC'] + ds['PRECL']).isel(time=xxx) * xxx * xxx
et_day = ds['QFLX'].isel(time=xxx) * xxx
t_c = ds['TREFHT'].isel(time=xxx) - xxx
pet_day = xxx * xxx * (t_c + xxx) * np.sqrt(np.abs(t_c))
eli = (pet_day - et_day) / (p_day + xxx)
p_mean = p_day.mean()
risk = (p_day - p_mean) / p_mean * xxx
mask = ds['LANDFRAC'].isel(time=xxx) > xxx
x = risk.where(mask).values.flatten()
y = eli.where(mask).values.flatten()
valid = ~np.isnan(x) & ~np.isnan(y) & ~np.isinf(y)
x, y = (x[valid], y[valid])
fig, ax = plt.subplots(figsize=(xxx, xxx), dpi=xxx)
colors = np.where(y >= xxx, np.where(x >= xxx, '#xxxAxxxE', '#Dxxx'), np.where(x >= xxx, '#xxxFCxxxFxxx', '#FFxxx'))
ax.scatter(x, y, c=colors, s=xxx, alpha=xxx, edgecolors='none', zorder=xxx)
ax.axhline(xxx, color='black', linewidth=xxx, linestyle='--', zorder=xxx)
ax.axvline(xxx, color='black', linewidth=xxx, linestyle='--', zorder=xxx)
text_style = dict(fontsize=xxx, fontweight='bold')
ax.text(-xxx, xxx, 'Regime xxx\nMoisture-limited, Low Rainfall\nNot Statistically Significant', color='#xxx', **text_style, va='top')
ax.text(xxx, xxx, 'Regime xxx\nMoisture-limited, High Rainfall', color='#xxx', **text_style, va='top')
ax.text(-xxx, -xxx, 'Regime xxx\nEnergy-limited, Low Rainfall', color='#xxx', **text_style, va='bottom')
ax.text(xxx, -xxx, 'Regime xxx\nEnergy-limited,\nHigh Rainfall', color='#xxx', **text_style, va='bottom')
ax.set_xlabel('Relative Risk of Heatwaves (Rainfall Conditions)', fontsize=xxx, fontweight='bold')
ax.set_ylabel('Evaporative Limiting Index (ELI)', fontsize=xxx, fontweight='bold')
ax.set_xlim(-xxx, xxx)
ax.set_ylim(-xxx, xxx)
ax.tick_params(direction='in', length=xxx, width=xxx, labelsize=xxx)
ax.grid(True, linestyle=':', alpha=xxx)
plt.tight_layout()
plt.savefig('./regime_plot_with_text.pdf', bbox_inches='tight', dpi=xxx)
plt.savefig('./regime_plot_with_text.png', bbox_inches='tight', dpi=xxx)
plt.show()
print('搞定！四个象限的文字已经加上，且散点大小已调大。')
