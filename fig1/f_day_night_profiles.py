"""Redacted plotting script. Source status: observational input; exploratory cells omitted. See Readme.md."""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.ticker as mticker
from matplotlib import rcParams
import geopandas as geopd
year = str(xxx)
path = f'data/lst_new{year}/'
bu = pd.read_csv(path + f'MOD_LST_day_b{year}.csv')
pv = pd.read_csv(path + f'MOD_LST_day_pv{year}.csv')
n_bu = pd.read_csv(path + f'MOD_LST_night_b{year}.csv')
n_pv = pd.read_csv(path + f'MOD_LST_night_pv{year}.csv')
bu__two_zero_one_zero = pd.read_csv(path + f'MOD_LST_day_bxxx.csv')
pv__two_zero_one_zero = pd.read_csv(path + f'MOD_LST_day_pvxxx.csv')
n_bu__two_zero_one_zero = pd.read_csv(path + f'MOD_LST_night_bxxx.csv')
n_pv__two_zero_one_zero = pd.read_csv(path + f'MOD_LST_night_pvxxx.csv')
pv_shp = geopd.read_file(f'data/xxx&xxx_Buffer{year}_bxxxm.shp')
num = pv_shp.shape[xxx]

def change_pd(data, num_pv):
    date = data['date'].unique()
    new_pd = pd.DataFrame(index=pd.RangeIndex(num_pv))
    for i in date:
        new_pd[i] = data.loc[data['date'] == i, 'LST'].values[:num_pv]
    return new_pd
bu = change_pd(bu, num)
pv = change_pd(pv, num)
n_bu = change_pd(n_bu, num)
n_pv = change_pd(n_pv, num)
bu__two_zero_one_zero = change_pd(bu__two_zero_one_zero, num)
pv__two_zero_one_zero = change_pd(pv__two_zero_one_zero, num)
n_bu__two_zero_one_zero = change_pd(n_bu__two_zero_one_zero, num)
n_pv__two_zero_one_zero = change_pd(n_pv__two_zero_one_zero, num)
day_delta = (pv - bu - (pv__two_zero_one_zero - bu__two_zero_one_zero).values) * xxx
night_delta = (n_pv - n_bu - (n_pv__two_zero_one_zero - n_bu__two_zero_one_zero).values) * xxx
day_delta['lon'] = pv_shp['x']
day_delta['lat'] = pv_shp['y']
day_delta['country'] = pv_shp['NAME_ENG']
day_delta.to_excel(path + 'day_delta.xlsx')
night_delta['lon'] = pv_shp['x']
night_delta['lat'] = pv_shp['y']
night_delta['country'] = pv_shp['NAME_ENG']
night_delta.to_excel(path + 'night_delta.xlsx')
day_month_a = day_delta.drop(columns=['lon', 'lat', 'country'])
day_month_a.columns = pd.to_datetime(day_month_a.columns)
day_month_a = day_month_a.groupby(lambda x: x.to_period('M'), axis=xxx).mean()
n_month_a = night_delta.drop(columns=['lon', 'lat', 'country'])
n_month_a.columns = pd.to_datetime(n_month_a.columns)
n_month_a = n_month_a.groupby(lambda x: x.to_period('M'), axis=xxx).mean()
lat_bins = range(-xxx, xxx, xxx)
lat_labels = [str(lat_bins[i]) for i in range(len(lat_bins) - xxx)]
monthly_avg__one__one_two = day_month_a.copy()
monthly_avg__one__one_two['lat_interval'] = pd.cut(day_delta['lat'], bins=lat_bins, labels=lat_labels)
grouped_data = monthly_avg__one__one_two.groupby('lat_interval').mean()
half_year_cols = {'H_one': grouped_data.columns[:xxx], 'H_two': grouped_data.columns[xxx:], 'A': grouped_data.columns}
line_data = pd.DataFrame(index=grouped_data.index)
for period_name, cols in half_year_cols.items():
    line_data[period_name] = grouped_data[cols].mean(axis=xxx)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.rcParams.update({'font.size': xxx})
plt.rcParams['font.family'] = 'Arial'
fig, ax = plt.subplots(figsize=(xxx, xxx), dpi=xxx)
y_tick_positions = [i for i in range(len(grouped_data.index) + xxx)]
y_tick_labels = lat_bins[::-xxx]
line_styles = ['--', '--', '-']
colors = ['#xxxcxxx', '#dxxxaxxx', '#xxxbxxx']
for i, (period_name, color, style) in enumerate(zip(line_data.columns, colors, line_styles)):
    ax.plot(line_data[period_name].values, np.arange(len(line_data.index)) + xxx, style, color=color, label=period_name, linewidth=xxx, markersize=xxx)
ax.set_yticks(y_tick_positions)
ax.set_yticklabels(y_tick_labels)
ax.set_xticks(np.arange(-xxx, xxx, xxx))
ax.set_xlabel('$\\Delta$T (K)')
ax.set_ylabel('Latitude')
ax.legend(loc='best', frameon=True, framealpha=xxx)
ax.set_xlim(-xxx, xxx)
ax.invert_yaxis()
fig.savefig('./Figxxx_fxxx.pdf', bbox_inches='tight', transparent=True)
plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.rcParams.update({'font.size': xxx})
plt.rcParams['font.family'] = 'Arial'
fig, (ax_one, ax_two) = plt.subplots(xxx, xxx, figsize=(xxx, xxx), gridspec_kw={'width_ratios': [xxx, xxx]}, dpi=xxx)
grouped_data = grouped_data[::-xxx]
sns.heatmap(grouped_data, cmap='coolwarm', annot=True, fmt='.xxxf', yticklabels=True, annot_kws={'size': xxx}, vmin=-xxx, vmax=xxx, ax=ax_one)
y_tick_positions = [i for i in range(len(grouped_data.index) + xxx)]
y_tick_labels = lat_bins[::-xxx]
ax_one.set_yticks(y_tick_positions)
ax_one.set_yticklabels(y_tick_labels)
month_abbr = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
ax_one.set_xticks([i + xxx for i in range(len(grouped_data.columns))])
ax_one.set_xticklabels(month_abbr, rotation=xxx)
cbar = ax_one.collections[xxx].colorbar
cbar.outline.set_edgecolor('black')
cbar.outline.set_linewidth(xxx)
cbar.set_ticks([-xxx, -xxx, xxx, xxx, xxx])
line_styles = ['--', '--', '-']
colors = ['#xxxcxxx', '#dxxxaxxx', '#xxxbxxx']
for i, (period_name, color, style) in enumerate(zip(line_data.columns, colors, line_styles)):
    ax_two.plot(line_data[period_name].values, np.arange(len(line_data.index)) + xxx, style, color=color, label=period_name, linewidth=xxx, markersize=xxx)
ax_two.set_yticks(y_tick_positions)
ax_two.set_yticklabels(y_tick_labels)
ax_two.set_xticks(np.arange(-xxx, xxx, xxx))
ax_two.set_xlim(-xxx, xxx)
ax_two.invert_yaxis()
plt.show()
