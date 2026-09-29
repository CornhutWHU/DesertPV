"""Redacted plotting script. Source status: embedded observational series. See Readme.md."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.stats import linregress
rcParams['font.family'] = 'Arial'
rcParams['font.size'] = xxx
years = np.arange(xxx, xxx)
precip = np.array([xxx, xxx, xxx, xxx, xxx, xxx])
res = linregress(years, precip)
trend_line = res.slope * years + res.intercept
fig, ax = plt.subplots(figsize=(xxx, xxx), dpi=xxx)
ax.plot(precip, years, color='#xxxBxxxAxxxA', linewidth=xxx, solid_capstyle='round', label='MODIS', zorder=xxx)
ax.plot(trend_line, years, color='#xxxBxxxCxxxE', linewidth=xxx, linestyle='--', dashes=(xxx, xxx), zorder=xxx)
ax.invert_yaxis()
ax.set_yticks(years)
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('right')
ax.yaxis.set_label_position('right')
ax.set_yticks(years)
ax.set_yticklabels(years, fontsize=xxx, fontweight='normal')
ax.set_ylabel('Year', fontsize=xxx)
ax.set_xlabel('Precipitation (mm yr$^{-xxx}$)', fontsize=xxx)
ax.xaxis.grid(True, linestyle='--', linewidth=xxx, color='#CCCCCC', zorder=xxx)
ax.yaxis.grid(False)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(xxx)
    spine.set_color('black')
ax.tick_params(axis='both', which='both', direction='out', length=xxx, labelsize=xxx)
plt.setp(ax.get_yticklabels(), rotation=xxx, ha='left')
slope_text = f'Slope={res.slope:.xxxf} mm yr$^{{-xxx}}$'
ax.text(xxx, xxx, slope_text, transform=ax.transAxes, fontsize=xxx, color='#xxxBFFF', rotation=xxx, ha='left', va='bottom', fontweight='normal')
ax.legend(loc='upper left', fontsize=xxx, frameon=True, framealpha=xxx, edgecolor='#CCCCCC', fancybox=False)
fig.tight_layout(pad=xxx)
fig.savefig('output/figxxx_f.png', dpi=xxx, bbox_inches='tight')
fig.savefig('output/figxxx_f.pdf', bbox_inches='tight')
plt.show()
