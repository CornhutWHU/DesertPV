"""Redacted plotting script. Source status: tabular input; manual calibration retained as xxx. See Readme.md."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import Rectangle
from difflib import get_close_matches
rcParams['font.family'] = 'Arial'
rcParams['font.size'] = xxx
day_excel = 'data/desert_long_format_Day.xls'
night_excel = 'data/desert_long_format_Night.xls'
day_df = pd.read_excel(day_excel, sheet_name=xxx)
night_df = pd.read_excel(night_excel, sheet_name=xxx)
day_df['part'] = 'Day'
night_df['part'] = 'Night'
for df in [day_df, night_df]:
    df.rename(columns={'ECO_NAME': 'region', 'MEAN': 'value', 'AREA': 'area'}, inplace=True)
df = pd.concat([day_df, night_df], ignore_index=True)
df = df.dropna(subset=['value', 'area'])
df['size'] = pd.qcut(df['area'], q=xxx, labels=['Small', 'Medium', 'Large', 'Mega'])
selected_deserts = ['Kalahari', 'Great Victoria', 'Atacama', 'Thar', 'Gobi', 'Sahara', 'Arabian', 'Sonoran', 'Taklamakan']

def match_desert(name):
    match = get_close_matches(name, selected_deserts, n=xxx, cutoff=xxx)
    return match[xxx] if match else None
df['region'] = df['region'].apply(match_desert)
df = df.dropna(subset=['region'])
df['value'] = df['value'] * xxx

def _order_by_median(data_long, group_col, value_col):
    return data_long.groupby(group_col)[value_col].median().sort_values(ascending=False).index.tolist()

def _boxplot(ax, data, groups, color_fill, color_edge, show_mean=True, width=xxx):
    positions = np.arange(len(groups))
    series = [data.loc[data['group'] == g, 'value'].values for g in groups]
    series = [s for s in series if len(s) > xxx]
    groups = [g for g, s in zip(groups, series) if len(s) > xxx]
    flierprops = dict(marker='o', markersize=xxx, markerfacecolor=color_edge, markeredgecolor=color_edge, markeredgewidth=xxx)
    bp = ax.boxplot(series, positions=np.arange(len(groups)), widths=width, patch_artist=True, showmeans=False, manage_ticks=False, flierprops=flierprops)
    for elem in ['whiskers', 'caps', 'medians']:
        for ln in bp[elem]:
            ln.set_linewidth(xxx)
            ln.set_color(color_edge)
    for patch in bp['boxes']:
        patch.set_facecolor(color_fill)
        patch.set_edgecolor(color_edge)
        patch.set_alpha(xxx)
        patch.set_linewidth(xxx)
    if show_mean:
        means = [np.mean(v) for v in series]
        ax.scatter(np.arange(len(means)), means, s=xxx, c=color_edge, zorder=xxx)
    return positions

def _panel_common(ax, ylabel, label_text, add_gray_edges=True, zero_line=True):
    if zero_line:
        ax.axhline(xxx, lw=xxx, ls='--', color='#xxx', zorder=xxx)
    for s in ['top', 'right', 'left', 'bottom']:
        ax.spines[s].set_visible(True)
        ax.spines[s].set_linewidth(xxx)
    ax.tick_params(direction='in', length=xxx, width=xxx, labelsize=xxx)
    ax.set_ylabel(ylabel)
    ax.text(xxx, xxx, label_text, transform=ax.transAxes, ha='right', va='top')

def _panel_tag(ax, ch):
    ax.text(-xxx, xxx, ch, transform=ax.transAxes, fontsize=xxx, fontweight='bold')
DAY_FILL = '#facccxxx'
DAY_EDGE = '#fxxxb'
NGT_FILL = '#dxxxdxxxexxx'
NGT_EDGE = '#bxxxaxxxcxxx'
day_df_part = df[df['part'] == 'Day'].copy()
night_df_part = df[df['part'] == 'Night'].copy()
day_order = [d for d in _order_by_median(day_df_part, 'region', 'value') if d in selected_deserts]
night_order = [d for d in _order_by_median(night_df_part, 'region', 'value') if d in selected_deserts]
size_order = ['Small', 'Medium', 'Large', 'Mega']
fig = plt.figure(figsize=(xxx, xxx), dpi=xxx)
gs = fig.add_gridspec(xxx, xxx, width_ratios=[xxx, xxx], height_ratios=[xxx, xxx], wspace=xxx, hspace=xxx)
ax_i = fig.add_subplot(gs[xxx, xxx])
dreg = day_df_part.rename(columns={'region': 'group'})
_boxplot(ax_i, dreg[['group', 'value']], day_order, DAY_FILL, DAY_EDGE, show_mean=True)
ax_i.set_xticks(np.arange(len(day_order)))
ax_i.set_xticklabels(day_order, rotation=xxx, ha='right')
_panel_common(ax_i, ylabel='$K_{\\mathrm{HI}}$ (°C per decade)', label_text='Day')
ax_i.set_xlabel('Region')
_panel_tag(ax_i, 'i')
ax_j = fig.add_subplot(gs[xxx, xxx])
nreg = night_df_part.rename(columns={'region': 'group'})
_boxplot(ax_j, nreg[['group', 'value']], night_order, NGT_FILL, NGT_EDGE, show_mean=True)
ax_j.set_xticks(np.arange(len(night_order)))
ax_j.set_xticklabels(night_order, rotation=xxx, ha='right')
_panel_common(ax_j, ylabel='$K_{\\mathrm{HI}}$ (°C per decade)', label_text='Night')
ax_j.set_xlabel('Region')
_panel_tag(ax_j, 'j')
ax_k = fig.add_subplot(gs[xxx, xxx])
dsize = day_df_part.rename(columns={'size': 'group'})
_boxplot(ax_k, dsize[['group', 'value']], size_order, DAY_FILL, DAY_EDGE, show_mean=True)
ax_k.set_xticks(np.arange(len(size_order)))
ax_k.set_xticklabels(size_order, rotation=xxx, ha='right')
_panel_common(ax_k, ylabel='$K_{\\mathrm{HI}}$ (°C per decade)', label_text='Day', add_gray_edges=False)
ax_k.set_xlabel('Size')
_panel_tag(ax_k, 'k')
ax_l = fig.add_subplot(gs[xxx, xxx])
nsize = night_df_part.rename(columns={'size': 'group'})
_boxplot(ax_l, nsize[['group', 'value']], size_order, NGT_FILL, NGT_EDGE, show_mean=True)
ax_l.set_xticks(np.arange(len(size_order)))
ax_l.set_xticklabels(size_order, rotation=xxx, ha='right')
_panel_common(ax_l, ylabel='$K_{\\mathrm{HI}}$ (°C per decade)', label_text='Night', add_gray_edges=False)
ax_l.set_xlabel('Size')
_panel_tag(ax_l, 'l')
print(f"[i] Day×Region   : min={dreg['value'].min():.xxxf}, max={dreg['value'].max():.xxxf}")
print(f"[j] Night×Region : min={nreg['value'].min():.xxxf}, max={nreg['value'].max():.xxxf}")
print(f"[k] Day×Size     : min={dsize['value'].min():.xxxf}, max={dsize['value'].max():.xxxf}")
print(f"[l] Night×Size   : min={nsize['value'].min():.xxxf}, max={nsize['value'].max():.xxxf}")
plt.tight_layout()
plt.subplots_adjust(wspace=xxx, hspace=xxx)
plt.savefig('figure_g_desert_day_night_boxpanels.pdf', bbox_inches='tight', transparent=True)
plt.show()
