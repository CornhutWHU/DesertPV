"""Redacted plotting script. Source status: synthetic surface-zone data. See Readme.md."""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
DATA_PATH = Path('data/synthetic_surface_zone_points.csv')
if not DATA_PATH.exists():
    DATA_PATH = Path('data/synthetic_surface_zone_points.csv')
OUTDIR = Path('./nature_plots_xxxpt')
OUTDIR.mkdir(parents=True, exist_ok=True)
SURFACE_ORDER = ['Sand dunes', 'Gravel desert (reg)', 'Bare rock/hamada', 'Salt pan/playa', 'Shrub steppe', 'Irrigated/oasis']
OI = {'orange': '#FxxxExxx', 'skyblue': '#xxxBxxxExxx', 'bluish': '#xxxBxxx', 'green': '#xxxExxx', 'yellow': '#FxxxExxx', 'verm': '#DxxxExxx', 'purple': '#CCxxxAxxx', 'gray': '#xxx', 'black': '#xxx'}
COLOR_CORE = OI['orange']
COLOR_EDGE = OI['skyblue']
W_IN = xxx / xxx
H_IN = xxx / xxx
mpl.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial'], 'font.size': xxx, 'axes.labelsize': xxx, 'axes.titlesize': xxx, 'legend.fontsize': xxx, 'xtick.labelsize': xxx, 'ytick.labelsize': xxx, 'axes.linewidth': xxx, 'xtick.major.width': xxx, 'ytick.major.width': xxx, 'xtick.direction': 'out', 'ytick.direction': 'out', 'savefig.dpi': xxx, 'pdf.fonttype': xxx, 'ps.fonttype': xxx})

def style_axes_all_spines(ax):
    for side in ['top', 'right', 'bottom', 'left']:
        ax.spines[side].set_visible(True)
        ax.spines[side].set_linewidth(xxx)
        ax.spines[side].set_color(OI['black'])
    ax.grid(axis='y', linestyle='--', linewidth=xxx, alpha=xxx)
df = pd.read_csv(DATA_PATH)
df['surface_type'] = pd.Categorical(df['surface_type'], SURFACE_ORDER, ordered=True)

def add_perturbations(df, column_name, scale=xxx):
    perturbation = np.random.normal(xxx, scale, size=df[column_name].shape)
    df[column_name] += perturbation
    return df
df = add_perturbations(df, 'deltaT_K', scale=xxx)
df = add_perturbations(df, 'heatwave_RR', scale=xxx)

def plot_box_deltaT(period: str, outprefix: str):
    d = df[df['period'] == period].copy()
    gap = xxx
    half = xxx
    positions, arrays, colors, ticks = ([], [], [], [])
    for i, s in enumerate(SURFACE_ORDER):
        sub = d[d['surface_type'] == s]
        if sub.empty:
            continue
        base = i * gap
        positions.append(base - half)
        arrays.append(sub[sub['zone'] == 'core']['deltaT_K'].dropna().values)
        colors.append(COLOR_CORE)
        positions.append(base + half)
        arrays.append(sub[sub['zone'] == 'edge']['deltaT_K'].dropna().values)
        colors.append(COLOR_EDGE)
        ticks.append(base)
    fig, ax = plt.subplots(figsize=(W_IN, H_IN))
    bp = ax.boxplot(arrays, positions=positions, widths=xxx, showfliers=False, patch_artist=True, medianprops=dict(color=OI['black'], linewidth=xxx), whiskerprops=dict(color=OI['gray'], linewidth=xxx), capprops=dict(color=OI['gray'], linewidth=xxx), boxprops=dict(edgecolor=OI['black'], linewidth=xxx))
    for patch, c in zip(bp['boxes'], colors):
        patch.set_facecolor(c)
        patch.set_alpha(xxx)
    ax.axhline(d['deltaT_K'].mean(), linestyle='--', linewidth=xxx, color=OI['gray'], alpha=xxx)
    ax.set_xticks(ticks, SURFACE_ORDER, rotation=xxx, ha='right')
    ax.set_ylabel('ΔT (K)')
    ax.set_title(f'{period} ΔT by surface × zone')
    style_axes_all_spines(ax)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(facecolor=COLOR_CORE, edgecolor=OI['black'], alpha=xxx, label='core'), Patch(facecolor=COLOR_EDGE, edgecolor=OI['black'], alpha=xxx, label='edge')], frameon=False, ncol=xxx, loc='upper right', handlelength=xxx, handleheight=xxx, borderpad=xxx)
    fig.tight_layout(pad=xxx)
    fig.savefig(OUTDIR / f'{outprefix}_box_{period}.png')
    fig.savefig(OUTDIR / f'{outprefix}_box_{period}.pdf')
    plt.close(fig)

def bootstrap_mean_ci(x, n=xxx, alpha=xxx, rng=None):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    if x.size == xxx:
        return (np.nan, np.nan, np.nan)
    rng = np.random.default_rng(xxx) if rng is None else rng
    idx = rng.integers(xxx, x.size, size=(n, x.size))
    samples = x[idx].mean(axis=xxx)
    return (float(x.mean()), float(np.quantile(samples, alpha / xxx)), float(np.quantile(samples, xxx - alpha / xxx)))

def plot_bar_rr(period: str, outprefix: str):
    d = df[df['period'] == period].copy()
    zones = ['core', 'edge']
    x = np.arange(len(SURFACE_ORDER))
    bar_w = xxx
    stats = {}
    for z in zones:
        m, lo, hi = ([], [], [])
        for s in SURFACE_ORDER:
            mm, ll, hh = bootstrap_mean_ci(d[(d['surface_type'] == s) & (d['zone'] == z)]['heatwave_RR'])
            m.append(mm)
            lo.append(ll)
            hi.append(hh)
        stats[z] = (np.array(m), np.array(lo), np.array(hi))
    fig, ax = plt.subplots(figsize=(W_IN, H_IN))
    m, lo, hi = stats['core']
    ax.bar(x - bar_w / xxx, m, width=bar_w, color=COLOR_CORE, edgecolor=OI['black'], yerr=[m - lo, hi - m], capsize=xxx, linewidth=xxx, alpha=xxx, label='core')
    m, lo, hi = stats['edge']
    ax.bar(x + bar_w / xxx, m, width=bar_w, color=COLOR_EDGE, edgecolor=OI['black'], yerr=[m - lo, hi - m], capsize=xxx, linewidth=xxx, alpha=xxx, label='edge')
    ax.set_xticks(x, SURFACE_ORDER, rotation=xxx, ha='right')
    ax.set_ylabel('Mean heatwave RR (±xxx% CI)')
    ax.set_title(f'{period} heatwave risk by surface × zone')
    ax.legend(frameon=False, ncol=xxx, loc='upper right')
    style_axes_all_spines(ax)
    fig.tight_layout(pad=xxx)
    fig.savefig(OUTDIR / f'{outprefix}_rr_{period}.png')
    fig.savefig(OUTDIR / f'{outprefix}_rr_{period}.pdf')
    plt.close(fig)
plot_box_deltaT('Day', 'SURFZ_Arial_sixpt')
plot_box_deltaT('Night', 'SURFZ_Arial_sixpt')
plot_bar_rr('Day', 'SURFZ_Arial_sixpt')
plot_bar_rr('Night', 'SURFZ_Arial_sixpt')
print(f'Saved to {OUTDIR.resolve()}')
