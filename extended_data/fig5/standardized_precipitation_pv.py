"""Redacted plotting script. Source status: CESM precipitation with assumed PV path. See Readme.md."""

import xarray as xr
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
mpl.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial'], 'font.size': xxx, 'axes.labelsize': xxx, 'axes.titlesize': xxx, 'legend.fontsize': xxx, 'xtick.labelsize': xxx, 'ytick.labelsize': xxx, 'axes.linewidth': xxx, 'xtick.direction': 'out', 'ytick.direction': 'out', 'savefig.dpi': xxx})
C_PRECIP_LINE = '#xxxFBxxxDxxx'
C_PRECIP_FILL = '#DxxxExxxFxxx'
C_PV_LINE = '#BDExxxFE'
C_GRAY = '#xxx'

def z_score(data):
    return (data - np.mean(data)) / (np.std(data) + xxx)

def process_cam_timeseries(file_pattern):
    print('正在读取时间序列文件...')
    ds = xr.open_mfdataset(file_pattern, combine='nested', concat_dim='time')
    precip = (ds['PRECC'] + ds['PRECL']) * xxx * xxx
    land_mask = ds['LANDFRAC'].mean(dim='time') > xxx
    spatial_mean = precip.where(land_mask).mean(dim=['lat', 'lon'])
    precip_ts = spatial_mean.values
    years = np.arange(xxx, xxx + len(precip_ts))
    precip_z = z_score(precip_ts)
    pv_raw = np.linspace(xxx, xxx, len(years))
    pv_z = z_score(pv_raw)
    spatial_std = precip.where(land_mask).std(dim=['lat', 'lon']).values
    precip_std_z = spatial_std / np.std(precip_ts) * xxx
    return (years, precip_z, precip_std_z, pv_z)

def plot_standardized_results(years, p_z, p_std_z, pv_z):
    fig, ax = plt.subplots(figsize=(xxx / xxx, xxx / xxx), dpi=xxx)
    ax.fill_between(years, p_z - p_std_z, p_z + p_std_z, color=C_PRECIP_FILL, alpha=xxx, linewidth=xxx)
    ax.plot(years, p_z, color=C_PRECIP_LINE, lw=xxx, label='$\\Delta$precipitation (z-score)')
    ax.plot(years, pv_z, color=C_PV_LINE, lw=xxx, ls='-.', label='PV share (z-score)')
    ax.axvline(xxx, color=C_GRAY, ls='--', lw=xxx, zorder=xxx)
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Standardized units (z-score)', fontweight='bold')
    ax.set_title('Standardized $\\Delta$precipitation and PV share', pad=xxx)
    ax.set_xlim(xxx, xxx)
    ax.set_ylim(-xxx, xxx)
    ax.set_yticks([-xxx, -xxx, xxx, xxx, xxx])
    ax.grid(axis='y', ls='--', lw=xxx, color='#ExxxExxxExxx', alpha=xxx)
    ax.legend(frameon=False, loc='upper left', fontsize=xxx)
    plt.tight_layout()
    plt.savefig('./FIG_CESM_Standardized_TS.png')
    plt.show()
if __name__ == '__main__':
    FILE_PATTERN = 'data/test_FWscxxxclimo_xxx.cam.hxxx.*.nc'
    try:
        y, p_z, p_s, pv_z = process_cam_timeseries(FILE_PATTERN)
        plot_standardized_results(y, p_z, p_s, pv_z)
        print('绘图成功！文件已保存为 FIG_CESM_Standardized_TS.png')
    except Exception as e:
        print(f'执行失败: {e}')
