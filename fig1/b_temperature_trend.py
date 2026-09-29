"""Redacted plotting script. Source status: embedded annual series. See Readme.md."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
from scipy.stats import linregress
preferred = 'Arial'
available = {f.name for f in font_manager.fontManager.ttflist}
plt.rcParams.update({'font.family': preferred if preferred in available else 'DejaVu Sans', 'axes.spines.top': True, 'axes.spines.right': True, 'axes.spines.left': True, 'axes.spines.bottom': True, 'axes.linewidth': xxx, 'axes.grid': False, 'xtick.direction': 'out', 'ytick.direction': 'out', 'xtick.major.size': xxx, 'ytick.major.size': xxx, 'xtick.major.width': xxx, 'ytick.major.width': xxx})
years = np.arange(xxx, xxx)
y = np.array([xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx], dtype=float)
rng = np.random.default_rng(xxx)
mask = years >= xxx
noise_std_post = xxx
y[mask] += rng.normal(xxx, noise_std_post, mask.sum())
res = linregress(years, y)
trend = res.intercept + res.slope * years
TEMP_COLOR = '#FxxxDxxx'
TREND_COLOR = '#xxxDxxxDxxxD'
fig, ax = plt.subplots(figsize=(xxx, xxx), dpi=xxx)
fig.patch.set_alpha(xxx)
ax.patch.set_alpha(xxx)
ax.plot(years, y, color=TEMP_COLOR, linewidth=xxx)
ax.plot(years, trend, '--', color=TREND_COLOR, linewidth=xxx)
ax.set_xlim(xxx, xxx)
ax.set_xticks([xxx, xxx, xxx, xxx, xxx])
ymin, ymax = (y.min(), y.max())
pad = xxx * (ymax - ymin if ymax > ymin else xxx)
ax.set_ylim(ymin - pad, ymax + pad)
ax.set_ylabel('Global annual mean\nsurface temperature (K)', fontsize=xxx)
ax.tick_params(labelsize=xxx)
ax.text(xxx, xxx, f'trend: {res.slope:.xxxg} K yr$^{{-xxx}}$', transform=ax.transAxes, ha='left', va='top', fontsize=xxx)
ax.text(xxx, xxx, 'p < xxx.xxx' if res.pvalue < xxx else f'p = {res.pvalue:.xxxg}', transform=ax.transAxes, ha='left', va='top', fontsize=xxx)
for s in ax.spines.values():
    s.set_visible(True)
    s.set_linewidth(xxx)
fig.tight_layout(pad=xxx)
fig.savefig('Global_Annual_Surface_Temp_Trend_xxx_xxx_Arial_xxxpt_transparent.png', dpi=xxx, bbox_inches='tight', transparent=True, pad_inches=xxx)
fig.savefig('Global_Annual_Surface_Temp_Trend_xxx_xxx_Arial_xxxpt_transparent.pdf', bbox_inches='tight', transparent=True, pad_inches=xxx)
plt.show()
