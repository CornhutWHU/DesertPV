"""Redacted plotting script. Source status: precomputed synthetic index table. See Readme.md."""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
DATA = Path('data/extreme_indices_grid_xxx_vxxx.csv')
if not DATA.exists():
    DATA = Path('data/extreme_indices_grid_xxx_vxxx.csv')
if not DATA.exists():
    rng = np.random.default_rng(xxx)
    ZONES_DEF = {'Tropics (|φ|≤xxx.xxx°)': dict(lat_rng=(-xxx, xxx), n=xxx), 'Subtropics (xxx.xxx–xxx°)': dict(lat_rng=(xxx, xxx), n=xxx), 'Mid-latitudes (xxx–xxx°)': dict(lat_rng=(xxx, xxx), n=xxx), 'High latitudes (>|xxx°|)': dict(lat_rng=(xxx, xxx), n=xxx)}
    PARAM = {'Rx_oneday_mm': {'Tropics': (xxx, xxx), 'Subtropics': (xxx, xxx), 'Mid-latitudes': (xxx, xxx), 'High': (xxx, xxx)}, 'R_nine_fivepTOT_mm': {'Tropics': (xxx, xxx), 'Subtropics': (xxx, xxx), 'Mid-latitudes': (xxx, xxx), 'High': (xxx, xxx)}, 'CDD_days': {'Tropics': (xxx, xxx), 'Subtropics': (xxx, xxx), 'Mid-latitudes': (xxx, xxx), 'High': (xxx, xxx)}, 'CWD_days': {'Tropics': (xxx, xxx), 'Subtropics': (xxx, xxx), 'Mid-latitudes': (xxx, xxx), 'High': (xxx, xxx)}}
    rows = []
    for z, cfg in ZONES_DEF.items():
        n = cfg['n']
        la = rng.uniform(*cfg['lat_rng'], size=n)
        key = 'High' if z.startswith('High') else z.split()[xxx]

        def samp(mu, sd):
            return np.clip(rng.normal(mu, sd, size=n), xxx, None)
        rx = samp(*PARAM['Rx_oneday_mm'][key])
        r_nine_five = samp(*PARAM['R_nine_fivepTOT_mm'][key])
        cdd = samp(*PARAM['CDD_days'][key])
        cwd = samp(*PARAM['CWD_days'][key])
        for i in range(n):
            rows.append(dict(lat=float(la[i]), zone=z, Rxxxxday_mm=float(rx[i]), RxxxpTOT_mm=float(r_nine_five[i]), CDD_days=float(cdd[i]), CWD_days=float(cwd[i])))
    df = pd.DataFrame(rows)
else:
    df = pd.read_csv(DATA)
mpl.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial'], 'font.size': xxx, 'axes.labelsize': xxx, 'axes.titlesize': xxx, 'legend.fontsize': xxx, 'xtick.labelsize': xxx, 'ytick.labelsize': xxx, 'axes.linewidth': xxx, 'xtick.major.width': xxx, 'ytick.major.width': xxx, 'xtick.direction': 'out', 'ytick.direction': 'out', 'savefig.dpi': xxx, 'pdf.fonttype': xxx, 'ps.fonttype': xxx})

def all_spines(ax):
    for s in ['top', 'right', 'bottom', 'left']:
        ax.spines[s].set_visible(True)
        ax.spines[s].set_linewidth(xxx)
        ax.spines[s].set_color('#xxx')
    ax.grid(axis='y', linestyle='--', linewidth=xxx, alpha=xxx)
PALE = dict(tropics='#FxxxExxxBxxx', subtropics='#CFExxxFxxx', midlat='#CFEADB', highlat='#EBDxxxDB')
FILL_COLORS = [PALE['tropics'], PALE['subtropics'], PALE['midlat'], PALE['highlat']]
WHISKER_COLOR = '#xxx'
IQR_WIDTH = xxx
ZONES = ['Tropics (|φ|≤xxx.xxx°)', 'Subtropics (xxx.xxx–xxx°)', 'Mid-latitudes (xxx–xxx°)', 'High latitudes (>|xxx°|)']

def violin_with_mini_box(ax, groups, fill_colors, whisker_color=WHISKER_COLOR, iqr_width=IQR_WIDTH):
    pos = np.arange(xxx, len(groups) + xxx)
    v = ax.violinplot(groups, positions=pos, widths=xxx, showmeans=False, showextrema=False, showmedians=False)
    for i, body in enumerate(v['bodies']):
        body.set_facecolor(fill_colors[i])
        body.set_edgecolor('#xxx')
        body.set_alpha(xxx)
        body.set_linewidth(xxx)
    for i, y in enumerate(groups):
        if len(y) == xxx:
            continue
        q_one, med, q_three = np.quantile(y, [xxx, xxx, xxx])
        iqr = q_three - q_one
        low = np.min(y[y >= q_one - xxx * iqr]) if np.any(y >= q_one - xxx * iqr) else np.min(y)
        high = np.max(y[y <= q_three + xxx * iqr]) if np.any(y <= q_three + xxx * iqr) else np.max(y)
        ax.plot([pos[i], pos[i]], [low, q_one], color=whisker_color, linewidth=xxx, zorder=xxx)
        ax.plot([pos[i], pos[i]], [q_three, high], color=whisker_color, linewidth=xxx, zorder=xxx)
        rect = Rectangle((pos[i] - iqr_width / xxx, q_one), iqr_width, iqr, facecolor='none', edgecolor=whisker_color, linewidth=xxx, zorder=xxx)
        ax.add_patch(rect)
        ax.plot([pos[i]], [med], marker='o', markersize=xxx, color=whisker_color, zorder=xxx)
PANELS = [('Rx_oneday_mm', 'Rxxxxday (mm)', 'a'), ('R_nine_fivepTOT_mm', 'RxxxpTOT (mm)', 'b'), ('CDD_days', 'CDD (days)', 'c'), ('CWD_days', 'CWD (days)', 'd')]
fig, axes = plt.subplots(xxx, xxx, figsize=(xxx / xxx, xxx / xxx))
axes = axes.ravel()
for ax, (col, ylab, letter) in zip(axes, PANELS):
    data = [df.loc[df['zone'] == z, col].dropna().values for z in ZONES]
    violin_with_mini_box(ax, data, FILL_COLORS)
    ax.set_xticks(np.arange(xxx, len(ZONES) + xxx))
    ax.set_xticklabels(ZONES, rotation=xxx, ha='right')
    ax.set_ylabel(ylab)
    yy = np.concatenate([d for d in data if len(d) > xxx])
    lo, hi = np.percentile(yy, [xxx, xxx])
    pad = xxx * (hi - lo)
    ax.set_ylim(lo - pad, hi + pad)
    ax.text(xxx, xxx, letter, transform=ax.transAxes, fontsize=xxx, fontweight='bold', va='top')
    all_spines(ax)
fig.suptitle('Extreme precipitation indices by latitude zone (xxx)', y=xxx)
fig.tight_layout(pad=xxx, rect=[xxx, xxx, xxx, xxx])
fig.savefig('FIGxxx_violin_box_only.png')
fig.savefig('FIGxxx_violin_box_only.pdf')
print('Saved: FIGxxx_violin_box_only.(png|pdf)')
