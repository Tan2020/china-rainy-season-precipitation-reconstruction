#!/usr/bin/env python
# coding: utf-8

# In[79]:


import numpy as np
import pandas as pd
# 相关系数和 NSE 计算函数
def calc_metrics(df):
    obs = df['obs'].values
    sim = df['sim'].values
    # 去掉 NaN
    mask = ~np.isnan(obs) & ~np.isnan(sim)
    obs = obs[mask]
    sim = sim[mask]
    if len(obs) == 0:
        return np.nan, np.nan
    # Pearson 相关系数
    corr = np.corrcoef(obs, sim)[0, 1]
    # NSE
    obs_mean = np.mean(obs)
    numerator = np.sum((sim - obs) ** 2)
    denominator = np.sum((obs - obs_mean) ** 2)
    nse = 1 - numerator / denominator if denominator != 0 else np.nan
    return corr, nse
# 对 7 个区域逐个计算
metrics = []
for reg_abbr in region_abbr:
    df_mean = region_series[reg_abbr]
    corr, nse = calc_metrics(df_mean)
    metrics.append({'region': reg_abbr, 'corr': corr, 'RE': nse})

metrics_df = pd.DataFrame(metrics)
print(metrics_df)


# In[82]:


import numpy as np

def calc_bias_for_year(df, year):
    row = df[df['year'] == year]
    if row.empty:
        return np.nan, np.nan
    obs = float(row['obs'])
    sim = float(row['sim'])
    abs_bias = obs - sim              # 观测减模拟，>0 表示模型低估
    rel_bias = abs_bias / obs * 100   # 相对偏差（%）
    return abs_bias, rel_bias

year = 2021

# 西北 NWC
df_nwc = region_series['NC']
abs_bias_nwc, rel_bias_nwc = calc_bias_for_year(df_nwc, year)
print(f'NC {year}: 绝对偏差 = {abs_bias_nwc:.2f} mm, 相对偏差 = {rel_bias_nwc:.2f}%')

# 华东 EC
df_ec = region_series['EC']
abs_bias_ec, rel_bias_ec = calc_bias_for_year(df_ec, year)
print(f'EC {year}: 绝对偏差 = {abs_bias_ec:.2f} mm, 相对偏差 = {rel_bias_ec:.2f}%')


# In[64]:


import pandas as pd
import os
import matplotlib.pyplot as plt

data1 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-2\第一轮2.xlsx')
folder = r'C:\Users\xiaotian\Desktop\data\model-2\pre1'

regions     = ["东北", "西北", "华北", "华东", "华中", "华南", "西南"]
region_abbr = ["NEC", "NWC", "NC", "EC", "CC", "SC", "SWC"]

color = '#b22222'
train_start, train_end = 1956, 2002
test_start,  test_end  = 2003, 2020

def load_station_data(param):
    train_file = os.path.join(folder, f'{param}_train_runoff.csv')
    test_file  = os.path.join(folder, f'{param}_test_runoff.csv')

    train = pd.read_csv(train_file).iloc[:, -2:]
    test  = pd.read_csv(test_file).iloc[:, -2:]

    train.columns = ['obs', 'sim']
    test.columns  = ['obs', 'sim']

    train['year'] = range(train_start, train_start + len(train))
    test['year']  = range(test_start,  test_start  + len(test))

    return pd.concat([train, test], ignore_index=True)

# 各区域 y 轴范围（下限, 上限）
y_limits = {
    'NEC': (200, 800),
    'NWC': (200, 500),
    'NC':  (100, 800),
    'EC':  (450, 1150),
    'CC':  (400, 1000),
    'SC':  (400, 1600),
    'SWC': (400, 900),
}

region_series = {}
for reg_cn, reg_abbr in zip(regions, region_abbr):
    df_reg = data1[data1['region'] == reg_cn][['name', 'canshu']]
    df_list = []
    for _, row in df_reg.iterrows():
        df = load_station_data(row['canshu'])
        df['station'] = row['name']
        df_list.append(df)
    df_all = pd.concat(df_list, ignore_index=True)
    df_mean = df_all.groupby('year')[['obs', 'sim']].mean().reset_index()
    region_series[reg_abbr] = df_mean


# In[77]:


import matplotlib.pyplot as plt
plt.rc('font', family='Times New Roman',weight='bold')
fig, axes = plt.subplots(4, 2, figsize=(12, 12), dpi=300)
axes = axes.flatten()
panel_labels = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)']
for i, (reg_abbr, label) in enumerate(zip(region_abbr, panel_labels)):
    ax = axes[i]
    df_mean = region_series[reg_abbr]
    line_obs, = ax.plot(df_mean['year'], df_mean['obs'],
                        color='k', lw=1.5, label='P Obs',alpha=0.9,ls='-.')
    line_sim, = ax.plot(df_mean['year'], df_mean['sim'],
                        color=color, lw=1.5, label='P Sim')
    ax.axvline(x=train_end + 0.5, color='black', lw=1)
    x_min, x_max = df_mean['year'].min(), df_mean['year'].max()
    ax.set_xlim(x_min - 2, x_max + 2)
    ax.set_xticks(range(1960, 2025, 13))
    ax.tick_params(axis='both', labelsize=13)
    ymin, ymax = y_limits[reg_abbr]
    ax.set_ylim(ymin, ymax)
    ax.set_ylabel('Precipitation(mm)', fontsize=13,weight='bold')
    ax.set_title(f'{label}  {reg_abbr}', fontsize=15, loc='left',weight='bold')
    left_leg = ax.legend(handles=[line_obs, line_sim],
                         labels=['P Obs', 'P Sim'],
                         loc='lower left',
                         bbox_to_anchor=(0.02, 0),
                         ncol=2,
                         frameon=False,
                         fontsize=12)
    right_leg = ax.legend(handles=[line_obs, line_sim],
                          labels=['P Obs', 'P Pred'],
                          loc='lower right',
                          bbox_to_anchor=(0.98, 0),
                          ncol=1,
                          frameon=False,
                          fontsize=12)
    ax.add_artist(left_leg)
fig.delaxes(axes[-1])
# 调整子图上下间距
plt.subplots_adjust(hspace=-0.10)  # 0.25 比默认小；想更挤可改成 0.2 或 0.15
plt.tight_layout()
plt.show()


# In[96]:


import pandas as pd
import os
import matplotlib.pyplot as plt

data1 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-1\第一轮7.xlsx')
folder = r'C:\Users\xiaotian\Desktop\data\model-1\pre1'

regions     = ["东北", "西北", "华北", "华东", "华中", "华南", "西南"]
region_abbr = ["NEC", "NWC", "NC", "EC", "CC", "SC", "SWC"]

color = '#b22222'
train_start, train_end = 1956, 2002
test_start,  test_end  = 2003, 2020

def load_station_data(param):
    train_file = os.path.join(folder, f'{param}_train_runoff.csv')
    test_file  = os.path.join(folder, f'{param}_test_runoff.csv')

    train = pd.read_csv(train_file).iloc[:, -2:]
    test  = pd.read_csv(test_file).iloc[:, -2:]

    train.columns = ['obs', 'sim']
    test.columns  = ['obs', 'sim']

    train['year'] = range(train_start, train_start + len(train))
    test['year']  = range(test_start,  test_start  + len(test))

    return pd.concat([train, test], ignore_index=True)

# 各区域 y 轴范围（下限, 上限）
y_limits = {
    'NEC': (400, 1000),
    'NWC': (300, 700),
    'NC':  (200, 1100),
    'EC':  (900, 1800),
    'CC':  (750, 1600),
    'SC':  (1000, 2400),
    'SWC': (700, 1100),
}

region_series = {}
for reg_cn, reg_abbr in zip(regions, region_abbr):
    df_reg = data1[data1['region'] == reg_cn][['name', 'canshu']]
    df_list = []
    for _, row in df_reg.iterrows():
        df = load_station_data(row['canshu'])
        df['station'] = row['name']
        df_list.append(df)
    df_all = pd.concat(df_list, ignore_index=True)
    df_mean = df_all.groupby('year')[['obs', 'sim']].mean().reset_index()
    region_series[reg_abbr] = df_mean


# In[97]:


import matplotlib.pyplot as plt
plt.rc('font', family='Times New Roman',weight='bold')
fig, axes = plt.subplots(4, 2, figsize=(12, 12), dpi=300)
axes = axes.flatten()
panel_labels = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)']
for i, (reg_abbr, label) in enumerate(zip(region_abbr, panel_labels)):
    ax = axes[i]
    df_mean = region_series[reg_abbr]
    line_obs, = ax.plot(df_mean['year'], df_mean['obs'],
                        color='k', lw=1.5, label='P Obs',alpha=0.9,ls='-.')
    line_sim, = ax.plot(df_mean['year'], df_mean['sim'],
                        color=color, lw=1.5, label='P Sim')
    ax.axvline(x=train_end + 0.5, color='black', lw=1)
    x_min, x_max = df_mean['year'].min(), df_mean['year'].max()
    ax.set_xlim(x_min - 2, x_max + 2)
    ax.set_xticks(range(1960, 2025, 13))
    ax.tick_params(axis='both', labelsize=13)
    ymin, ymax = y_limits[reg_abbr]
    ax.set_ylim(ymin, ymax)
    ax.set_ylabel('Precipitation(mm)', fontsize=13,weight='bold')
    ax.set_title(f'{label}  {reg_abbr}', fontsize=15, loc='left',weight='bold')
    left_leg = ax.legend(handles=[line_obs, line_sim],
                         labels=['P Obs', 'P Sim'],
                         loc='lower left',
                         bbox_to_anchor=(0.02, 0),
                         ncol=2,
                         frameon=False,
                         fontsize=12)
    right_leg = ax.legend(handles=[line_obs, line_sim],
                          labels=['P Obs', 'P Pred'],
                          loc='lower right',
                          bbox_to_anchor=(0.98, 0),
                          ncol=1,
                          frameon=False,
                          fontsize=12)
    ax.add_artist(left_leg)
fig.delaxes(axes[-1])
# 调整子图上下间距
plt.subplots_adjust(hspace=-0.10)  # 0.25 比默认小；想更挤可改成 0.2 或 0.15
plt.tight_layout()
plt.show()


# In[ ]:




