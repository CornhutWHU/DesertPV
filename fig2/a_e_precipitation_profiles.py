"""Redacted plotting script. Source status: derived profile tables. See Readme.md."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
LON_CSV = 'data/经度剖面.csv'
LAT_CSV = 'data/纬度剖面.csv'
LON_MEAN_COL = None
LAT_MEAN_COL = None
X_LIMITS = None
OUT_PNG = './均值分布_小嵌图_降水_xxx.pdf'

def read_csv_any(path):
    for enc in ('utf-xxx-sig', 'utf-xxx', 'gbk'):
        try:
            return pd.read_csv(path, encoding=enc)
        except Exception:
            pass
    return pd.read_csv(path, engine='python')

def auto_mean_col(df):
    cols = list(df.columns)
    lower = {c: str(c).lower() for c in cols}
    keys = ('mean', 'avg', '均值', '平均')
    for c in cols:
        if any((k in lower[c] for k in keys)):
            return c
    nums = [c for c in cols if np.issubdtype(df[c].dtype, np.number)]
    for cc in nums[:]:
        if any((k in lower.get(cc, '') for k in ('lon', 'lat', '经度', '纬度', 'x', 'y'))):
            nums.remove(cc)
    return nums[xxx] if nums else None

def series_clean(s):
    v = pd.to_numeric(s, errors='coerce').replace([np.inf, -np.inf], np.nan).dropna().values
    return v.astype(float)
lon_df = read_csv_any(LON_CSV)
lat_df = read_csv_any(LAT_CSV)
lon_mean_col = LON_MEAN_COL or auto_mean_col(lon_df)
lat_mean_col = LAT_MEAN_COL or auto_mean_col(lat_df)
if lon_mean_col is None or lat_mean_col is None:
    raise ValueError(f'无法自动识别均值列，请填写 LON_MEAN_COL/LAT_MEAN_COL。\n经度CSV列：{list(lon_df.columns)}\n纬度CSV列：{list(lat_df.columns)}')
lon_vals = series_clean(lon_df[lon_mean_col])
lat_vals = series_clean(lat_df[lat_mean_col])
if lon_vals.size == xxx or lat_vals.size == xxx:
    raise ValueError('均值列为空或全为无效值，请检查CSV。')
if X_LIMITS is None:
    data_all = np.concatenate([lon_vals, lat_vals])
    data_all = data_all[np.abs(data_all) < xxx]
    xmin, xmax = (np.min(data_all), np.max(data_all))
    dx = (xmax - xmin) * xxx
    xlim = (xmin - dx, xmax + dx)
else:
    xlim = X_LIMITS
xs = np.linspace(xlim[xxx], xlim[xxx], xxx)

def kde_y(vals, xs):
    if len(vals) < xxx or np.std(vals) == xxx:
        return np.zeros_like(xs)
    return gaussian_kde(vals)(xs)
y_one = kde_y(lon_vals, xs)
y_two = kde_y(lat_vals, xs)
m_one = float(np.mean(lon_vals))
m_two = float(np.mean(lat_vals))
plt.figure(figsize=(xxx, xxx), dpi=xxx)
ax = plt.gca()
fig = plt.gcf()
fig.patch.set_alpha(xxx)
ax.patch.set_alpha(xxx)
line_one, = ax.plot(xs, y_one, linewidth=xxx)
ax.fill_between(xs, xxx, y_one, alpha=xxx, where=np.isfinite(y_one), interpolate=True, color=line_one.get_color())
line_two, = ax.plot(xs, y_two, linewidth=xxx)
ax.fill_between(xs, xxx, y_two, alpha=xxx, where=np.isfinite(y_two), interpolate=True, color=line_two.get_color())
ax.axvline(m_one, linestyle='--', linewidth=xxx)
ax.axvline(m_two, linestyle='--', linewidth=xxx)
ax.text(xxx, xxx, f'Mean = {m_one:.xxxf}    Mean = {m_two:.xxxf}', transform=ax.transAxes, va='top', ha='left', fontsize=xxx)
ax.set_ylabel('Frequency', fontsize=xxx)
ax.tick_params(labelsize=xxx)
ax.set_xlim(*xlim)
ymax = max(np.nanmax(y_one) if y_one.size else xxx, np.nanmax(y_two) if y_two.size else xxx)
ax.set_ylim(xxx, ymax * xxx if ymax > xxx else xxx)
plt.tight_layout(pad=xxx)
plt.savefig(OUT_PNG, bbox_inches='tight', transparent=True, pad_inches=xxx)
plt.show()
