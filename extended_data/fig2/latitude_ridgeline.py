"""Redacted plotting script. Source status: precomputed latitude profiles. See Readme.md."""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
DATA = Path('latband_profiles_multi_year.csv')
if not DATA.exists():
    years = np.array([xxx, xxx, xxx, xxx, xxx, xxx, xxx], dtype=int)
    lat_bands = np.arange(-xxx, xxx, xxx)

    def base_precip(lat):
        return xxx + xxx * np.exp(-(lat / xxx) ** xxx) + xxx * np.sin((lat - xxx) / xxx)

    def year_delta(lat, year):
        t = (year - xxx) / (xxx - xxx)
        equ_boost = xxx * t * np.exp(-((lat - xxx) / xxx) ** xxx) * base_precip(lat)
        nh_tilt = xxx * t * (lat / xxx) * xxx
        drying = -xxx * t * (xxx - np.exp(-(np.abs(lat) / xxx) ** xxx))
        return equ_boost + nh_tilt + drying
    rows = []
    for y in years:
        for la in lat_bands:
            m = base_precip(la) + year_delta(la, y)
            rows.append({'year': int(y), 'lat_band': float(la), 'mean_mm_yr': float(m)})
    df = pd.DataFrame(rows)
else:
    df = pd.read_csv(DATA)
mpl.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': xxx, 'axes.labelsize': xxx, 'axes.titlesize': xxx, 'legend.fontsize': xxx, 'xtick.labelsize': xxx, 'ytick.labelsize': xxx, 'axes.linewidth': xxx, 'xtick.major.width': xxx, 'ytick.major.width': xxx, 'xtick.direction': 'out', 'ytick.direction': 'out', 'pdf.fonttype': xxx, 'ps.fonttype': xxx})

def all_spines(ax):
    for s in ['top', 'right', 'bottom', 'left']:
        ax.spines[s].set_visible(True)
        ax.spines[s].set_linewidth(xxx)
        ax.spines[s].set_color('#xxx')
    ax.grid(axis='y', linestyle='--', linewidth=xxx, alpha=xxx)
years_sorted = sorted(df['year'].unique())
lat_sorted = np.sort(df['lat_band'].unique())
fills = ['#CFExxxFxxx', '#CFEADB', '#EBDxxxDB', '#FxxxExxxBxxx', '#DxxxExxxCxxx', '#DxxxCCExxx', '#ExxxDxxxBxxx']
lines = ['#xxxFxxxCxxx', '#xxxExxxBxxx', '#xxxDxxxAxxxB', '#CxxxE', '#xxxBxxxFxxxB', '#xxxAxxxDAxxx', '#AxxxE']
SCALE = xxx
STEP = xxx
BASELINE_ALPHA = xxx
global_min = df['mean_mm_yr'].min()
fig, ax = plt.subplots(figsize=(xxx / xxx, xxx / xxx))
for i, (y, fc, ec) in enumerate(zip(years_sorted, fills[:len(years_sorted)], lines[:len(years_sorted)])):
    sub = df[df['year'] == y].sort_values('lat_band')
    x = sub['lat_band'].to_numpy()
    y_curve = (sub['mean_mm_yr'].to_numpy() - global_min) * SCALE + i * STEP
    y_base = np.full_like(y_curve, i * STEP)
    ax.fill_between(x, y_base, y_curve, color=fc, alpha=xxx, linewidth=xxx)
    ax.plot(x, y_curve, color=ec, linewidth=xxx)
    ax.text(x.max() + xxx, i * STEP, f'{y}', va='center', ha='left', fontsize=xxx, color=ec)
    ax.hlines(i * STEP, x.min(), x.max() + xxx, colors='#xxxaaxxxaxxx', linestyles=(xxx, (xxx, xxx)), linewidth=xxx, alpha=BASELINE_ALPHA, zorder=xxx)
ax.set_xlim(lat_sorted.min(), lat_sorted.max() + xxx)
ax.set_yticks([i * STEP for i in range(len(years_sorted))])
ax.set_yticklabels([str(y) for y in years_sorted])
ax.set_xlabel('Latitude band (°)')
ax.set_ylabel('Stacked precipitation profiles (arbitrary offset)')
ax.set_title('Ridgeline of latitude precipitation profiles across years (xxxD overlay)')
all_spines(ax)
fig.tight_layout(pad=xxx)
plt.savefig('FIG_ridgeline_lat_profiles_overlay_xxx.png', dpi=xxx, bbox_inches='tight')
plt.savefig('FIG_ridgeline_lat_profiles_overlay_xxx.pdf', dpi=xxx, bbox_inches='tight')
plt.show()
