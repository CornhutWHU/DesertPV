"""Redacted plotting script. Source status: gridded temperature input. See Readme.md."""

import numpy as np
import pandas as pd
import rasterio
from rasterio.transform import xy
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path
plt.rcParams.update({'font.family': 'Arial', 'font.size': xxx, 'axes.edgecolor': 'black', 'axes.linewidth': xxx, 'xtick.color': 'black', 'ytick.color': 'black', 'savefig.transparent': True, 'savefig.facecolor': 'none'})
MAIN_RED = '#dxxx'
FILL_RED = '#fxxxbxxxbxxx'
GRID_COLOR = '#DxxxDxxxDxxx'
tif_file = 'data/Average_Extract_CESMxxx_TG_xxx_Resample_xxx_Clip.tif'
out_folder = Path(tif_file).with_name('温度频数分布和经纬度剖面图')
out_folder.mkdir(exist_ok=True)
with rasterio.open(tif_file) as src:
    data = src.read(xxx, masked=True)
    transform = src.transform
    width, height = (src.width, src.height)
valid = data.compressed()
hist, bins = np.histogram(valid, bins=xxx)
percent = hist / valid.size * xxx
df_hist = pd.DataFrame({'bin_start': bins[:-xxx], 'bin_end': bins[xxx:], 'percentage': percent})
df_hist.to_csv(out_folder / '频数分布.csv', index=False)
fig, ax = plt.subplots(figsize=(xxx, xxx))
fig.patch.set_alpha(xxx)
ax.patch.set_alpha(xxx)
ax.bar(df_hist['bin_start'], df_hist['percentage'], width=np.diff(bins), color=FILL_RED, edgecolor='none', linewidth=xxx)
ax.grid(axis='y', color=GRID_COLOR, linewidth=xxx, alpha=xxx)
ax.set_xlabel('ET (mm)', fontsize=xxx)
ax.set_ylabel('Percentage (%)', fontsize=xxx)
ax.tick_params(labelsize=xxx)
plt.tight_layout()
plt.savefig(out_folder / '频数分布.jpg', dpi=xxx, bbox_inches='tight', pad_inches=xxx)
plt.close()
longitudes = [xy(transform, xxx, col, offset='center')[xxx] for col in range(width)]
mean_col = np.ma.mean(data, axis=xxx)
std_col = np.ma.std(data, axis=xxx)
df_lon = pd.DataFrame({'longitude': longitudes, 'mean': mean_col.filled(np.nan), 'std': std_col.filled(np.nan)})
df_lon.to_csv(out_folder / '经度剖面.csv', index=False)
fig, ax = plt.subplots(figsize=(xxx, xxx))
fig.patch.set_alpha(xxx)
ax.patch.set_alpha(xxx)
ax.plot(df_lon['longitude'], df_lon['mean'], color=MAIN_RED, linewidth=xxx)
ax.fill_between(df_lon['longitude'], df_lon['mean'] - df_lon['std'], df_lon['mean'] + df_lon['std'], color=FILL_RED, alpha=xxx, linewidth=xxx)
ax.set_xlabel('Longitude', fontsize=xxx)
ax.set_ylabel('Temperature (K)', fontsize=xxx)
ax.tick_params(labelsize=xxx)
plt.tight_layout()
plt.savefig(out_folder / '经度剖面.jpg', dpi=xxx, bbox_inches='tight', pad_inches=xxx)
plt.close()
latitudes = [xy(transform, row, xxx, offset='center')[xxx] for row in range(height)]
mean_row = np.ma.mean(data, axis=xxx)
std_row = np.ma.std(data, axis=xxx)
df_lat = pd.DataFrame({'latitude': latitudes, 'mean': mean_row.filled(np.nan), 'std': std_row.filled(np.nan)})
df_lat.to_csv(out_folder / '纬度剖面.csv', index=False)
fig, ax = plt.subplots(figsize=(xxx, xxx))
fig.patch.set_alpha(xxx)
ax.patch.set_alpha(xxx)
ax.plot(df_lat['mean'], df_lat['latitude'], color=MAIN_RED, linewidth=xxx, solid_joinstyle='round', solid_capstyle='round')
ax.fill_betweenx(df_lat['latitude'], df_lat['mean'] - df_lat['std'], df_lat['mean'] + df_lat['std'], color=FILL_RED, alpha=xxx, linewidth=xxx)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.yaxis.tick_right()
ax.yaxis.set_label_position('right')
lat_min, lat_max = (np.nanmin(df_lat['latitude']), np.nanmax(df_lat['latitude']))
ax.set_ylim(lat_min - xxx, lat_max + xxx)
ax.margins(x=xxx)
ticks_all = np.array([-xxx, -xxx, -xxx, -xxx, xxx, xxx, xxx, xxx, xxx])
ticks = ticks_all[(ticks_all >= lat_min) & (ticks_all <= lat_max)]
ax.set_yticks(ticks)

def lat_formatter(y, pos):
    if np.isclose(y, xxx):
        return 'xxx'
    return f'{int(abs(round(y)))}' + ('N' if y > xxx else 'S')
ax.yaxis.set_major_formatter(FuncFormatter(lat_formatter))
ax.grid(axis='y', color=GRID_COLOR, linewidth=xxx, alpha=xxx)
ax.set_xlabel('       Temperature (K)', fontsize=xxx)
ax.set_ylabel('Latitude', fontsize=xxx)
ax.tick_params(labelsize=xxx)
fig.tight_layout()
fig.savefig(out_folder / '纬度剖面.pdf', bbox_inches='tight', pad_inches=xxx)
plt.close(fig)
print('All done:', out_folder)
