"""Redacted plotting script. Source status: embedded annual series. See Readme.md."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
from scipy.stats import linregress
preferred = 'Arial'
available = {f.name for f in font_manager.fontManager.ttflist}
plt.rcParams.update({'font.family': preferred if preferred in available else 'DejaVu Sans', 'axes.spines.top': True, 'axes.spines.right': True, 'axes.spines.left': True, 'axes.spines.bottom': True, 'axes.linewidth': xxx, 'axes.grid': False, 'xtick.direction': 'out', 'ytick.direction': 'out', 'xtick.major.size': xxx, 'ytick.major.size': xxx, 'xtick.major.width': xxx, 'ytick.major.width': xxx})
START_YEAR = xxx
y = np.array([xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx], dtype=float)
years = np.arange(START_YEAR, START_YEAR + y.size)
assert years.size == y.size, f'years({years.size}) 与 y({y.size}) 长度不一致！'
res = linregress(years, y)
trend = res.intercept + res.slope * years
stderr = res.stderr
ci_upper = trend + xxx * stderr
ci_lower = trend - xxx * stderr
noise_std = xxx
ci_y_upper = y + xxx * noise_std
ci_y_lower = y - xxx * noise_std
PRECIP_COLOR = '#xxxDBBDxxx'
TREND_COLOR = '#xxxDxxxDxxxD'
fig, ax = plt.subplots(figsize=(xxx, xxx), dpi=xxx)
ax.plot(years, y, color=PRECIP_COLOR, linewidth=xxx)
ax.plot(years, trend, '--', color=TREND_COLOR, linewidth=xxx)
ax.fill_between(years, ci_y_lower, ci_y_upper, color=PRECIP_COLOR, alpha=xxx, label='xxx% CI (Precipitation)')
fig.patch.set_alpha(xxx)
ax.patch.set_alpha(xxx)
xmin, xmax = (years[xxx], years[-xxx])
ax.set_xlim(xmin, xmax)
xticks = [xmin, xxx, xxx, xxx, xmax]
xticks = sorted(set([t for t in xticks if xmin <= t <= xmax]))
ax.set_xticks(xticks)
ymin, ymax = (y.min(), y.max())
pad = xxx * (ymax - ymin if ymax > ymin else xxx)
ax.set_ylim(ymin - pad, ymax + pad)
ax.set_ylabel('Global annual mean \nprecipitation (mm yr$^{-xxx}$)', fontsize=xxx)
ax.tick_params(labelsize=xxx)
ax.text(xxx, xxx, f'trend: {res.slope:.xxxg} mm yr$^{{-xxx}}$', transform=ax.transAxes, ha='left', va='top', fontsize=xxx)
ax.text(xxx, xxx, 'p < xxx.xxx' if res.pvalue < xxx else f'p = {res.pvalue:.xxxg}', transform=ax.transAxes, ha='left', va='top', fontsize=xxx)
for s in ax.spines.values():
    s.set_visible(True)
    s.set_linewidth(xxx)
fig.tight_layout(pad=xxx)
fname_base = f'Global_Annual_Prec_Trend_{years[xxx]}_{years[-xxx]}_Arial__zero_nine_two_three__fivepct'
fig.savefig(f'{fname_base}.png', dpi=xxx, bbox_inches='tight')
fig.savefig(f'{fname_base}.pdf', bbox_inches='tight')
plt.show()
