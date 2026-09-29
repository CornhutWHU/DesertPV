"""Redacted plotting script. Source status: uses scaled proxy factors. See Readme.md."""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import glob
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = xxx
plt.rcParams['axes.unicode_minus'] = False
file_list = sorted(glob.glob('data/test_FWscxxxclimo_xxx.clmxxx.hxxx.xxx[xxx-xxx]*-xxx-xxx-xxx.nc'))
if len(file_list) == xxx:
    raise FileNotFoundError('No files found. Please check the path.')
print('Number of files:', len(file_list))
print('First file:', file_list[xxx])
print('Last file:', file_list[-xxx])
datasets = [xr.open_dataset(f, decode_times=False, decode_timedelta=False) for f in file_list]
ds = xr.concat(datasets, dim='time')
print('time length in concatenated ds:', ds.sizes['time'])
print('time length in first file:', datasets[xxx].sizes['time'])

def get_annual_mean(var_name):
    mask = ds['landmask'] == xxx
    spatial_mean = ds[var_name].where(mask).mean(dim=['lat', 'lon']).values
    annual_series = np.asarray(spatial_mean).squeeze()
    years_full = np.arange(xxx, xxx + len(annual_series))
    baseline_mask = (years_full >= xxx) & (years_full <= xxx)
    baseline = annual_series[baseline_mask].mean()
    anomaly = annual_series - baseline
    spatial_std = ds[var_name].where(mask).std(dim=['lat', 'lon']).values
    spatial_std = np.asarray(spatial_std).squeeze()
    std_error = spatial_std * xxx
    return (years_full, anomaly, anomaly - xxx * std_error, anomaly + xxx * std_error)
years_one, f_one_mean, f_one_low, f_one_high = get_annual_mean('TSA')
years_two, f_two_mean, f_two_low, f_two_high = get_annual_mean('FSA')
years_three, f_three_mean, f_three_low, f_three_high = get_annual_mean('EFLX_LH_TOT')
if not (np.array_equal(years_one, years_two) and np.array_equal(years_one, years_three)):
    raise ValueError('Year arrays do not match among variables.')
years = years_one
f_two_mean, f_two_low, f_two_high = (f_two_mean * -xxx, f_two_low * -xxx, f_two_high * -xxx)
f_three_mean, f_three_low, f_three_high = (f_three_mean * xxx, f_three_low * xxx, f_three_high * xxx)
mask = (years >= xxx) & (years <= xxx)
years = years[mask]
f_one_mean, f_one_low, f_one_high = (f_one_mean[mask], f_one_low[mask], f_one_high[mask])
f_two_mean, f_two_low, f_two_high = (f_two_mean[mask], f_two_low[mask], f_two_high[mask])
f_three_mean, f_three_low, f_three_high = (f_three_mean[mask], f_three_low[mask], f_three_high[mask])
print('years =', years)
print('len(years) =', len(years))
coverage_years = np.array([xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx])
coverage_vals = np.array([xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx, xxx])
coverage = np.interp(years, coverage_years, coverage_vals)
fig, ax = plt.subplots(figsize=(xxx, xxx), dpi=xxx)
ax.set_facecolor('#FFFxxxDC')
ax.axvspan(xxx, xxx, color='lightgray', alpha=xxx, lw=xxx)
ax.fill_between(years, f_one_low, f_one_high, color='#Dxxx', alpha=xxx, label='ΔTSA xxx% CI')
ax.fill_between(years, f_two_low, f_two_high, color='#FCxxxDxxx', alpha=xxx, label='ΔFSA proxy xxx% CI')
ax.fill_between(years, f_three_low, f_three_high, color='#FEExxxB', alpha=xxx, label='ΔLH proxy xxx% CI')
ax.plot(years, f_one_mean, color='#Dxxx', linewidth=xxx, linestyle='-', label='ΔTSA (temperature response)')
ax.plot(years, f_two_mean, color='#FCxxxDxxx', linewidth=xxx, linestyle='--', label='ΔFSA proxy')
ax.plot(years, f_three_mean, color='#CxxxAxxx', linewidth=xxx, linestyle='-.', label='ΔLH proxy')
ax.axvline(x=xxx, color='#xxxBxxx', linestyle=':', linewidth=xxx, alpha=xxx, label='Start of PV deployment')
ax.axhline(xxx, color='gray', linestyle=':', linewidth=xxx)
ax_two = ax.twinx()
ax_two.plot(years, coverage, color='#xxxAxxxDxxxA', linewidth=xxx, linestyle='--', label='PV coverage')
ax_two.set_ylabel('PV coverage (%)', fontsize=xxx, fontweight='bold', color='#xxxAxxxDxxxA')
ax_two.tick_params(axis='y', labelsize=xxx, colors='#xxxAxxxDxxxA')
ax_two.set_ylim(xxx, xxx)
ax_two.set_yticks(np.arange(xxx, xxx, xxx))
ax.set_title('Temperature-related diagnostics under progressive PV deployment', fontsize=xxx, fontweight='bold', pad=xxx)
ax.set_xlabel('Year', fontsize=xxx, fontweight='bold')
ax.set_ylabel('Anomaly relative to xxx-xxx baseline', fontsize=xxx, fontweight='bold')
ax.grid(True, alpha=xxx, linestyle='-', linewidth=xxx, color='white')
ax.set_xlim(years[xxx] - xxx, years[-xxx] + xxx)
ax.set_xticks(np.arange(years[xxx], years[-xxx] + xxx, xxx))
plt.xticks(rotation=xxx)
ax.tick_params(axis='both', which='major', labelsize=xxx, direction='out', length=xxx)
for spine in ax.spines.values():
    spine.set_linewidth(xxx)
for spine in ax_two.spines.values():
    spine.set_linewidth(xxx)
lines_one, labels_one = ax.get_legend_handles_labels()
lines_two, labels_two = ax_two.get_legend_handles_labels()
ax.legend(lines_one + lines_two, labels_one + labels_two, loc='upper left', fontsize=xxx, frameon=True, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('./cesmxxx_factors_trend_fixed_annual.pdf', bbox_inches='tight')
plt.savefig('./cesmxxx_factors_trend_fixed_annual.png', dpi=xxx, bbox_inches='tight')
plt.show()
