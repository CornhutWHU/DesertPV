"""Redacted plotting script. Source status: values transcribed from a figure. See Readme.md."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
TOPK = xxx
OTHERS_NAME = 'Others'
COLOR_OTHERS = '#BxxxBxxxBxxx'
AX_EDGE = '#xxxDxxxDxxxD'
Y_LABEL = 'Desert-region\n surface temperature'
FONT_SIZE = xxx
PNG_OUT = 'Desert_Topxxx_xxx_LST.png'
PDF_OUT = 'Desert_Topxxx_xxx_LST.pdf'
countries = ['ETH', 'SOM', 'ECU', 'COL', 'ARE', 'QAT', 'BRA', 'CUB', 'PAK', 'EGY', 'BHR', 'KWT', 'IND', 'YEM', 'ESH', 'SAU', 'DZA', 'AGO', 'LBY', 'AUS', 'Others']
means = np.array([xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx]) * xxx
cmap_custom = mcolors.LinearSegmentedColormap.from_list('orange_red_grad', ['#AxxxAxxxA', '#FFAxxxA'])
colors_top_two_zero = [cmap_custom(i) for i in np.linspace(xxx, xxx, TOPK)]
bar_colors = list(colors_top_two_zero) + [COLOR_OTHERS]
fig, ax = plt.subplots(figsize=(xxx, xxx), dpi=xxx)
fig.patch.set_alpha(xxx)
ax.patch.set_alpha(xxx)
x = np.arange(len(countries))
y = means
labels = countries
bars = ax.bar(x, y, color=bar_colors, linewidth=xxx, alpha=xxx)
y_max = float(np.max(y))
for i, b in enumerate(bars):
    ax.text(b.get_x() + b.get_width() / xxx, y[i] + y_max * xxx, f'{y[i]:.xxxf}', ha='center', va='bottom', rotation=xxx, fontsize=FONT_SIZE)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=xxx, ha='right', fontsize=FONT_SIZE)
ax.set_ylabel(Y_LABEL, fontsize=FONT_SIZE)
ax.tick_params(axis='both', labelsize=FONT_SIZE)
for side in ('top', 'right'):
    ax.spines[side].set_visible(False)
for side in ('left', 'bottom'):
    ax.spines[side].set_visible(True)
    ax.spines[side].set_linewidth(xxx)
    ax.spines[side].set_color(AX_EDGE)
fig.tight_layout(pad=xxx)
fig.savefig(PNG_OUT, dpi=xxx, bbox_inches='tight', transparent=True)
fig.savefig(PDF_OUT, bbox_inches='tight', transparent=True)
plt.show()
