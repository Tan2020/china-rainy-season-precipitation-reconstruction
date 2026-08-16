#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import gaussian_kde

plt.rc('font', family='Times New Roman', size=25)
# 读取数据
df = pd.read_excel(r"C:\Users\xiaotian\Desktop\data\验证\R_VR_contrast.xlsx", sheet_name=0)
# 需要的四组字段
cols = ['CXJ_R', 'RAP_R', 'CXJ_R1', 'Shi_R']
# 转成数值，无法识别的变为 NaN
for c in cols:
    df[c] = pd.to_numeric(df[c], errors='coerce')
# 分组数据
groups = [df[c].dropna().values for c in cols]
labels = ['CXJ_R', 'RAP_R', 'CXJ_R1', 'Shi_R']
main_color = 'darkblue'
# 创建画布
fig = plt.figure(figsize=(11, 5), dpi=300)
ax_box = fig.add_axes([0.08, 0.12, 0.88, 0.82])
# 避免空数组问题
plot_groups = [g if len(g)>0 else np.array([np.nan]) for g in groups]
# 画箱线图
box = ax_box.boxplot(plot_groups, positions=[1,2,3,4], widths=0.35,
    patch_artist=True, medianprops=dict(color='black', linewidth=2),
    boxprops=dict(color='black', linewidth=1.5),
    whiskerprops=dict(color='black', linewidth=1.5),
    capprops=dict(color='black', linewidth=1.5),
    flierprops=dict(marker='o', markersize=3, markerfacecolor='black', markeredgecolor='black'))
# 透明箱体
for p in box['boxes']:
    p.set_facecolor('none')
# 散点 + KDE 小提琴
rng = np.random.default_rng(0)
for x0, arr in zip([1,2,3,4], plot_groups):
    arr = arr[~np.isnan(arr)]
    if len(arr) == 0:
        continue
    sub = arr if len(arr)<=200 else rng.choice(arr, size=200, replace=False)
    ax_box.scatter( rng.normal(x0, 0.06, len(sub)), sub,
        s=18, alpha=0.8, color=main_color, edgecolors='none', zorder=3)
    # 小提琴（KDE）
    if len(arr) >= 5:
        y = np.linspace(arr.min(), arr.max(), 300)
        kde = gaussian_kde(arr)(y)
        kde = kde / kde.max() * 0.28
        ax_box.fill_betweenx(y, x0+0.22, x0+0.22+kde,   color=main_color, alpha=0.55)
        ax_box.plot(x0+0.22+kde, y, color=main_color, linewidth=1.2)
# 坐标等设置
labels = ['CXJ–P', 'RAP–P', 'CXJ–P′', 'Shi–P′']
ax_box.set_xticklabels(labels)
ax_box.set_xticks([1,2,3,4])
ax_box.set_xticklabels(labels)
ax_box.set_ylabel('R')
ax_box.axhline(0, color='k', linestyle='--', linewidth=1)
ax_box.set_ylim(-0.1, 1)
ax_box.set_xlim(0.5, 4.5)
ax_box.spines['top'].set_visible(False)
ax_box.spines['right'].set_visible(False)
plt.show()


# In[2]:


medians = [m.get_ydata()[0] for m in box['medians']]
for lab, med in zip(labels, medians):
    print(f'{lab} 中位数: {med:.3f}')


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import gaussian_kde

plt.rc('font', family='Times New Roman', size=25)
# 读取数据
df = pd.read_excel(r"C:\Users\xiaotian\Desktop\data\验证\R_VR_contrast.xlsx", sheet_name=0)
# 需要的四组字段
cols = ['CXJ_VR', 'RAP_VR', 'CXJ_VR1', 'Shi_VR']
# 转成数值，无法识别的变为 NaN
for c in cols:
    df[c] = pd.to_numeric(df[c], errors='coerce')
# 分组数据
groups = [df[c].dropna().values for c in cols]
labels = ['CXJ_VR', 'RAP_VR', 'CXJ_VR1', 'Shi_VR']
main_color = 'darkblue'
# 创建画布
fig = plt.figure(figsize=(11, 5), dpi=300)
ax_box = fig.add_axes([0.08, 0.12, 0.88, 0.82])
# 避免空数组问题
plot_groups = [g if len(g)>0 else np.array([np.nan]) for g in groups]
# 画箱线图
box = ax_box.boxplot(plot_groups, positions=[1,2,3,4], widths=0.35,
    patch_artist=True, medianprops=dict(color='black', linewidth=2),
    boxprops=dict(color='black', linewidth=1.5),
    whiskerprops=dict(color='black', linewidth=1.5),
    capprops=dict(color='black', linewidth=1.5),
    flierprops=dict(marker='o', markersize=3, markerfacecolor='black', markeredgecolor='black'))
# 透明箱体
for p in box['boxes']:
    p.set_facecolor('none')
# 散点 + KDE 小提琴
rng = np.random.default_rng(0)
for x0, arr in zip([1,2,3,4], plot_groups):
    arr = arr[~np.isnan(arr)]
    if len(arr) == 0:
        continue
    sub = arr if len(arr)<=200 else rng.choice(arr, size=200, replace=False)
    ax_box.scatter( rng.normal(x0, 0.06, len(sub)), sub,
        s=18, alpha=0.8, color=main_color, edgecolors='none', zorder=3)
    # 小提琴（KDE）
    if len(arr) >= 5:
        y = np.linspace(arr.min(), arr.max(), 300)
        kde = gaussian_kde(arr)(y)
        kde = kde / kde.max() * 0.28
        ax_box.fill_betweenx(y, x0+0.22, x0+0.22+kde,   color=main_color, alpha=0.55)
        ax_box.plot(x0+0.22+kde, y, color=main_color, linewidth=1.2)
# 坐标等设置
labels = ['CXJ–P', 'RAP–P', 'CXJ–P′', 'Shi–P′']
ax_box.set_xticklabels(labels)
ax_box.set_xticks([1,2,3,4])
ax_box.set_xticklabels(labels)
ax_box.set_ylabel('VR')
ax_box.axhline(1, color='k', linestyle='--', linewidth=1)
ax_box.set_ylim(0, 1.5)
ax_box.set_xlim(0.5, 4.5)
ax_box.spines['top'].set_visible(False)
ax_box.spines['right'].set_visible(False)
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import gaussian_kde

plt.rc('font', family='Times New Roman', size=25)
# 读取数据
df = pd.read_excel(r"C:\Users\xiaotian\Desktop\data\验证\R_VR_contrast.xlsx", sheet_name=0)
# 需要的四组字段
cols = ['CXJ_RE', 'RAP_RE', 'CXJ_RE1', 'Shi_RE']
# 转成数值，无法识别的变为 NaN
for c in cols:
    df[c] = pd.to_numeric(df[c], errors='coerce')
# 分组数据
groups = [df[c].dropna().values for c in cols]
labels = ['CXJ_VR', 'RAP_VR', 'CXJ_VR1', 'Shi_VR']
main_color = 'darkblue'
# 创建画布
fig = plt.figure(figsize=(11, 5), dpi=300)
ax_box = fig.add_axes([0.08, 0.12, 0.88, 0.82])
# 避免空数组问题
plot_groups = [g if len(g)>0 else np.array([np.nan]) for g in groups]
# 画箱线图
box = ax_box.boxplot(plot_groups, positions=[1,2,3,4], widths=0.35,
    patch_artist=True, medianprops=dict(color='black', linewidth=2),
    boxprops=dict(color='black', linewidth=1.5),
    whiskerprops=dict(color='black', linewidth=1.5),
    capprops=dict(color='black', linewidth=1.5),
    flierprops=dict(marker='o', markersize=3, markerfacecolor='black', markeredgecolor='black'))
# 透明箱体
for p in box['boxes']:
    p.set_facecolor('none')
# 散点 + KDE 小提琴
rng = np.random.default_rng(0)
for x0, arr in zip([1,2,3,4], plot_groups):
    arr = arr[~np.isnan(arr)]
    if len(arr) == 0:
        continue
    sub = arr if len(arr)<=200 else rng.choice(arr, size=200, replace=False)
    ax_box.scatter( rng.normal(x0, 0.06, len(sub)), sub,
        s=18, alpha=0.8, color=main_color, edgecolors='none', zorder=3)
    # 小提琴（KDE）
    if len(arr) >= 5:
        y = np.linspace(arr.min(), arr.max(), 300)
        kde = gaussian_kde(arr)(y)
        kde = kde / kde.max() * 0.28
        ax_box.fill_betweenx(y, x0+0.22, x0+0.22+kde,   color=main_color, alpha=0.55)
        ax_box.plot(x0+0.22+kde, y, color=main_color, linewidth=1.2)
# 坐标等设置
labels = ['CXJ–P', 'RAP–P', 'CXJ–P′', 'Shi–P′']
ax_box.set_xticklabels(labels)
ax_box.set_xticks([1,2,3,4])
ax_box.set_xticklabels(labels)
ax_box.set_ylabel('RE')
ax_box.axhline(0.3, color='k', linestyle='--', linewidth=1)
ax_box.axhline(0, color='k', linestyle='--', linewidth=1)
ax_box.set_ylim(-1.1, 1)
ax_box.set_xlim(0.5, 4.5)
ax_box.spines['top'].set_visible(False)
ax_box.spines['right'].set_visible(False)
plt.show()


# In[5]:


medians = [m.get_ydata()[0] for m in box['medians']]
for lab, med in zip(labels, medians):
    print(f'{lab} 中位数: {med:.3f}')


# In[ ]:





# In[11]:


import matplotlib.pyplot as plt
import pandas as pd
import shapefile
import numpy as np
import geopandas as gpd
sf = shapefile.Reader(r"C:\Users\xiaotian\Desktop\data\GIS\dilifenqv.shp")
all_sta = pd.read_csv(r'C:\Users\xiaotian\Desktop\data\验证\need_station.csv', encoding='gbk')
select_sta = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\验证\R_VR_contrast.xlsx', sheet_name=0)
select_sta = select_sta[['station', 'start_year']].dropna()
merge_sta = pd.merge(select_sta, all_sta, on='station', how='left')
merge_sta = merge_sta.dropna(subset=['lon', 'lat', 'start_year'])
main_color = 'darkblue'      # 主蓝色
light_color = 'darkblue'     # 浅蓝
point_color = '#111111'     # 深黑点
plt.rc('font', family='Times New Roman', size=20)
fig = plt.figure(figsize=(4.5, 7), dpi=300)
ax1 = fig.add_axes([0.10, 0.5, 0.85, 0.45])
# 画行政边界
for shape in sf.shapes():
    points = shape.points
    parts = list(shape.parts) + [len(points)]
    for i in range(len(parts) - 1):
        seg = points[parts[i]:parts[i + 1]]
        xs = [p[0] for p in seg]
        ys = [p[1] for p in seg]
        ax1.plot(xs, ys, color='black', linewidth=0.5, zorder=1)
ax1.scatter(all_sta['lon'],all_sta['lat'],
    s=10,color=point_color,edgecolors='none',zorder=3)
ax1.scatter(merge_sta['lon'],merge_sta['lat'],
    s=30,facecolors=point_color,edgecolors=main_color, alpha=0.5,linewidth=2,zorder=4)
ax1.set_xlim(70, 140)
ax1.set_ylim(17, 55)
xticks = range(75, 140, 15)
ax1.set_xticks(xticks)
ax1.set_xticklabels([f'{x}°E' for x in xticks], fontsize=20)
yticks = range(20, 55, 10)
ax1.set_yticks(yticks)
ax1.set_yticklabels([f'{y}°N' for y in yticks], fontsize=20)
ax1.set_title('(a)', fontsize=20, x=0.05)
# 调整刻度线字体大小
ax1.tick_params(axis='both', labelsize=20)



ax2 = fig.add_axes([0.10, 0.12, 0.85, 0.24])
years = np.arange(int(merge_sta['start_year'].min()), 2023)
cumulative = np.array([(merge_sta['start_year'] <= y).sum() for y in years])
ax2.step(years, cumulative, where='post', color=main_color, linewidth=2.0)
ax2.fill_between(years, cumulative, step='post', color=light_color, alpha=0.5)
ax2.set_xlim(1805, 2020)
ax2.set_ylim(0, 60)
ax2.set_xlabel('Year', fontsize=20)
ax2.set_ylabel('Number Stations', fontsize=20)
ax2.set_title('(b)', fontsize=20, x=0.05)
ax2.tick_params(axis='both', labelsize=20)
# 去掉上右边框
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

ax3_left, ax3_bottom, ax3_width, ax3_height = 0.788, 0.411, 0.16, 0.3
ax3 = fig.add_axes([ax3_left, ax3_bottom, ax3_width, ax3_height])
data1 = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\daoyv\Export_Output.shp")
data1.plot(ax=ax3, facecolor='whitesmoke', edgecolor='k', linewidth=0.2)
ax3.set_xlim(105, 125)   # 经度范围：大致南海区域
ax3.set_ylim(2, 25)      # 纬度范围：大致南海诸岛附近
ax3.set_xticks([])
ax3.set_yticks([])
for spine in ['right',]:
    ax3.spines[spine].set_visible(False)
ax3.tick_params(left=False, bottom=False)


plt.show()


# In[ ]:




