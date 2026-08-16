#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
plt.rc('font', family='Times New Roman', size=12)
fig = plt.figure(figsize=(4, 2), dpi=300)
left, bottom, width, height = 0.1, 0.1, 1, 1
ax = fig.add_axes([left, bottom, width, height])
# data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\china3.shp")

data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\dilifenqv.shp")

data.plot(ax=ax, facecolor='whitesmoke', edgecolor='k', linewidth=1)
station_data = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-1\第一轮7.xlsx')
cf = ax.scatter(station_data['lon'], station_data['lat'], c=station_data['test'], s=5, cmap='RdBu_r', vmax=1, vmin=0)
cbar = plt.colorbar(cf, pad=0.03)
cbar.set_label('RE')  
plt.ylim([17,55])
plt.xlim([70,136])
xticks = range(75, 136, 15)  
plt.xticks(xticks, [f'{x}°E' for x in xticks], fontsize=10)
yticks = range(20, 55, 10)  
plt.yticks(yticks, [f'{y}°N' for y in yticks], fontsize=10)
ax2_left, ax2_bottom, ax2_width, ax2_height =  0.26, 0.13, 0.18, 0.2
ax2 = fig.add_axes([ax2_left, ax2_bottom, ax2_width, ax2_height])
intervals = [0, 0.1, 0.2, 0.3,0.4,0.5,0.6, 0.7,0.8, 0.9,1.0]
counts = [((station_data['test'] >= intervals[i]) & (station_data['test'] < intervals[i+1])).sum() for i in range(len(intervals)-1)]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap((intervals[i] + intervals[i+1]) / 2) for i in range(len(intervals)-1)]
ax2.bar(range(len(counts)), counts, tick_label=[f'{intervals[i]}-{intervals[i+1]}' for i in range(len(intervals)-1)], color=colors,)
ax2.patch.set_alpha(0.2)  # 设置透明度
ax2.tick_params(axis='x', direction='in')
ax2.tick_params(axis='y', direction='in')
ax2.set_xticklabels([])
ax2.set_ylim([0,30])
ax2.set_xlim([0,10])
ax2.set_title('Number Statistics', y=0.80,size=8)
ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax3_left, ax3_bottom, ax3_width, ax3_height = 0.775, 0.10, 0.16, 0.3
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


# In[3]:


import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
plt.rc('font', family='Times New Roman', size=12)
fig = plt.figure(figsize=(4, 2), dpi=300)
left, bottom, width, height = 0.1, 0.1, 1, 1
ax = fig.add_axes([left, bottom, width, height])
# data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\china3.shp")

data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\dilifenqv.shp")

data.plot(ax=ax, facecolor='whitesmoke', edgecolor='k', linewidth=1)
station_data = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-1\第一轮7.xlsx')
cf = ax.scatter(station_data['lon'], station_data['lat'], c=station_data['test_corr'], s=5, cmap='RdBu_r', vmax=1, vmin=0)
cbar = plt.colorbar(cf, pad=0.03)
cbar.set_label('R')  
plt.ylim([17,55])
plt.xlim([70,136])
xticks = range(75, 136, 15)  
plt.xticks(xticks, [f'{x}°E' for x in xticks], fontsize=10)
yticks = range(20, 55, 10)  
plt.yticks(yticks, [f'{y}°N' for y in yticks], fontsize=10)
ax2_left, ax2_bottom, ax2_width, ax2_height =  0.26, 0.13, 0.18, 0.2
ax2 = fig.add_axes([ax2_left, ax2_bottom, ax2_width, ax2_height])
intervals = [0, 0.1, 0.2, 0.3,0.4,0.5,0.6, 0.7,0.8, 0.9,1.0]
counts = [((station_data['test_corr'] >= intervals[i]) & (station_data['test_corr'] < intervals[i+1])).sum() for i in range(len(intervals)-1)]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap((intervals[i] + intervals[i+1]) / 2) for i in range(len(intervals)-1)]
ax2.bar(range(len(counts)), counts, tick_label=[f'{intervals[i]}-{intervals[i+1]}' for i in range(len(intervals)-1)], color=colors,)
ax2.patch.set_alpha(0.2)  # 设置透明度
ax2.tick_params(axis='x', direction='in')
ax2.tick_params(axis='y', direction='in')
ax2.set_xticklabels([])
ax2.set_ylim([0,30])
ax2.set_xlim([0,10])
ax2.set_title('Number Statistics', y=0.80,size=8)
ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax3_left, ax3_bottom, ax3_width, ax3_height = 0.775, 0.10, 0.16, 0.3
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





# In[ ]:





# In[ ]:





# In[1]:


import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
plt.rc('font', family='Times New Roman', size=12)
fig = plt.figure(figsize=(4, 2), dpi=300)
left, bottom, width, height = 0.1, 0.1, 1, 1
ax = fig.add_axes([left, bottom, width, height])
# data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\china3.shp")
data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\dilifenqv.shp")
data.plot(ax=ax, facecolor='whitesmoke', edgecolor='k', linewidth=1)
station_data = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-2\第一轮2.xlsx')
cf = ax.scatter(station_data['lon'], station_data['lat'], c=station_data['test'], s=5, cmap='RdBu_r', vmax=1, vmin=0)
cbar = plt.colorbar(cf, pad=0.03)
cbar.set_label('RE')  
plt.ylim([17,55])
plt.xlim([70,136])
xticks = range(75, 136, 15)  
plt.xticks(xticks, [f'{x}°E' for x in xticks], fontsize=10)
yticks = range(20, 55, 10)  
plt.yticks(yticks, [f'{y}°N' for y in yticks], fontsize=10)
ax2_left, ax2_bottom, ax2_width, ax2_height =  0.26, 0.13, 0.18, 0.2
ax2 = fig.add_axes([ax2_left, ax2_bottom, ax2_width, ax2_height])
intervals = [0, 0.1, 0.2, 0.3,0.4,0.5,0.6, 0.7,0.8, 0.9,1.0]
counts = [((station_data['test'] >= intervals[i]) & (station_data['test'] < intervals[i+1])).sum() for i in range(len(intervals)-1)]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap((intervals[i] + intervals[i+1]) / 2) for i in range(len(intervals)-1)]
ax2.bar(range(len(counts)), counts, tick_label=[f'{intervals[i]}-{intervals[i+1]}' for i in range(len(intervals)-1)], color=colors,)
ax2.patch.set_alpha(0.2)  # 设置透明度
ax2.tick_params(axis='x', direction='in')
ax2.tick_params(axis='y', direction='in')
ax2.set_xticklabels([])
ax2.set_ylim([0,30])
ax2.set_xlim([0,10])
ax2.set_title('Number Statistics', y=0.80,size=8)
ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax3_left, ax3_bottom, ax3_width, ax3_height = 0.775, 0.10, 0.16, 0.3
ax3 = fig.add_axes([ax3_left, ax3_bottom, ax3_width, ax3_height])
# 在小图上再绘制一次同一 shapefile
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


# In[3]:


import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
plt.rc('font', family='Times New Roman', size=12)
fig = plt.figure(figsize=(4, 2), dpi=300)
left, bottom, width, height = 0.1, 0.1, 1, 1
ax = fig.add_axes([left, bottom, width, height])
# data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\china3.shp")
data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\dilifenqv.shp")
data.plot(ax=ax, facecolor='whitesmoke', edgecolor='k', linewidth=1)
station_data = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-2\第一轮2.xlsx')
cf = ax.scatter(station_data['lon'], station_data['lat'], c=station_data['test_corr'], s=5, cmap='RdBu_r', vmax=1, vmin=0)
cbar = plt.colorbar(cf, pad=0.03)
cbar.set_label('R')  
plt.ylim([17,55])
plt.xlim([70,136])
xticks = range(75, 136, 15)  
plt.xticks(xticks, [f'{x}°E' for x in xticks], fontsize=10)
yticks = range(20, 55, 10)  
plt.yticks(yticks, [f'{y}°N' for y in yticks], fontsize=10)
ax2_left, ax2_bottom, ax2_width, ax2_height =  0.26, 0.13, 0.18, 0.2
ax2 = fig.add_axes([ax2_left, ax2_bottom, ax2_width, ax2_height])
intervals = [0, 0.1, 0.2, 0.3,0.4,0.5,0.6, 0.7,0.8, 0.9,1.0]
counts = [((station_data['test_corr'] >= intervals[i]) & (station_data['test_corr'] < intervals[i+1])).sum() for i in range(len(intervals)-1)]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap((intervals[i] + intervals[i+1]) / 2) for i in range(len(intervals)-1)]
ax2.bar(range(len(counts)), counts, tick_label=[f'{intervals[i]}-{intervals[i+1]}' for i in range(len(intervals)-1)], color=colors,)
ax2.patch.set_alpha(0.2)  # 设置透明度
ax2.tick_params(axis='x', direction='in')
ax2.tick_params(axis='y', direction='in')
ax2.set_xticklabels([])
ax2.set_ylim([0,30])
ax2.set_xlim([0,10])
ax2.set_title('Number Statistics', y=0.80,size=8)
ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax3_left, ax3_bottom, ax3_width, ax3_height = 0.775, 0.10, 0.16, 0.3
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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[36]:


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
sequences = [np.random.rand(np.random.randint(7, 21)) for _ in range(14)]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap(i) for i in np.linspace(0, 1, 7)]
group_gap = 2
positions = []
for i in range(7):
    positions.extend([i * (2 + group_gap), i * (2 + group_gap) + 1])
plt.rc('font', family='Times New Roman', size=12)
fig, ax = plt.subplots(figsize=(4, 2), dpi=300)
bp = ax.boxplot(sequences, patch_artist=True, positions=positions)
for i in range(7):
    bp['boxes'][2 * i].set_facecolor(colors[i])
    bp['boxes'][2 * i + 1].set_facecolor(colors[i])
ax.set_ylabel('NSE')
ax.set_title('QIDADILIFENQV DUIBI')
ax.set_xticks(positions)
region_abbr = ["EC", "NC", "CC", "SC", "SWC", "NWC", "NEC"]
ax.set_xticks([pos for i, pos in enumerate(positions) if i % 2 == 0])
ax.set_xticklabels(region_abbr)
ax.set_xlim(-1, positions[-1] + 1)
plt.show()


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data1 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-2\第一轮2.xlsx')
data2 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-1\第一轮7.xlsx')
regions = ["东北", "西北","华北", "华东", "华中", "华南", "西南"]
region_abbr = ["NEC", "NWC","NC", "EC", "CC", "SC", "SWC"]
grouped_data1 = []
grouped_data2 = []
for region in regions:
    region_data1 = data1[data1['region'] == region]['test']
    region_data2 = data2[data2['region'] == region]['test']
    grouped_data1.append(region_data1)
    grouped_data2.append(region_data2)
all_grouped_data = []
for i in range(len(grouped_data1)):
    all_grouped_data.extend([grouped_data1[i], grouped_data2[i]])
cmap = plt.get_cmap('RdBu_r')
colors = [cmap(i) for i in np.linspace(0, 1, 7)]
colors1 = [(r, g, b, 0.7) for r, g, b, _ in colors]
colors2 = [(r, g, b, 1) for r, g, b, _ in colors]
all_colors = []
for i in range(len(colors1)):
    all_colors.extend([colors1[i], colors2[i]])
group_gap = 2
positions = []
for i in range(7):
    positions.extend([i * (2 + group_gap), i * (2 + group_gap) + 1])
plt.rc('font', family='Times New Roman', size=12)
fig, ax = plt.subplots(figsize=(4, 2), dpi=300)
bp = ax.boxplot(all_grouped_data, patch_artist=True, positions=positions)
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(all_colors[i])
# ax.set_ylabel('NSE')
ax.set_title('Year/Flood NSE')
ax.set_xticks([pos for i, pos in enumerate(positions) if i % 2 == 0])
ax.set_xticklabels(region_abbr)
ax.set_xlim(-1, positions[-1] + 1)
# legend_patches = [plt.Rectangle((0, 0), 1, 1, color=colors1[0], alpha=0.7),
#                   plt.Rectangle((0, 0), 1, 1, color=colors2[0], alpha=1)]
# ax.legend(legend_patches, ['Year', 'Flood'], loc='lower center', ncol=2,frameon=False)
plt.ylim([0.40,1])
plt.show()


# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data1 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-1\第一轮7.xlsx')
regions = ["东北", "西北", "华北", "华东", "华中", "华南", "西南"]
region_abbr = ["NEC", "NWC", "NC", "EC", "CC", "SC", "SWC"]
grouped_data1 = [data1[data1['region'] == region]['test'] for region in regions]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap(i) for i in np.linspace(0, 1, 7)]
colors1 = [(r, g, b, 0.8) for r, g, b, _ in colors]  # 统一透明度
positions = [i * 2 for i in range(len(grouped_data1))]
plt.rc('font', family='Times New Roman', size=12)
fig, ax = plt.subplots(figsize=(4, 2), dpi=300)
bp = ax.boxplot(grouped_data1, patch_artist=True, positions=positions)
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(colors1[i])
# ax.set_title('Year Precipitation NSE')
ax.set_xticks(positions)
ax.set_xticklabels(region_abbr)
ax.set_xlim(-1, positions[-1] + 1)
plt.ylabel('RE')
plt.ylim([0.40, 1])

plt.show()


# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data1 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-2\第一轮2.xlsx')
regions = ["东北", "西北", "华北", "华东", "华中", "华南", "西南"]
region_abbr = ["NEC", "NWC", "NC", "EC", "CC", "SC", "SWC"]
grouped_data1 = [data1[data1['region'] == region]['test'] for region in regions]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap(i) for i in np.linspace(0, 1, 7)]
colors1 = [(r, g, b, 0.8) for r, g, b, _ in colors]  # 统一透明度
positions = [i * 2 for i in range(len(grouped_data1))]
plt.rc('font', family='Times New Roman', size=12)
fig, ax = plt.subplots(figsize=(4, 2), dpi=300)
bp = ax.boxplot(grouped_data1, patch_artist=True, positions=positions)
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(colors1[i])
# ax.set_title('Summer Precipitation NSE')
ax.set_xticks(positions)
ax.set_xticklabels(region_abbr)
ax.set_xlim(-1, positions[-1] + 1)
plt.ylim([0.40, 1])
plt.ylabel('RE')
plt.show()


# In[ ]:





# In[ ]:





# In[61]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data1 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-2\第一轮2.xlsx')
data2 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-1\第一轮7.xlsx')
regions = ["东北", "西北","华北", "华东", "华中", "华南", "西南"]
region_abbr = ["NEC", "NWC","NC", "EC", "CC", "SC", "SWC"]
grouped_data1 = []
grouped_data2 = []
for region in regions:
    region_data1 = data1[data1['region'] == region]['test_corr']
    region_data2 = data2[data2['region'] == region]['test_corr']
    grouped_data1.append(region_data1)
    grouped_data2.append(region_data2)
all_grouped_data = []
for i in range(len(grouped_data1)):
    all_grouped_data.extend([grouped_data1[i], grouped_data2[i]])
cmap = plt.get_cmap('RdBu_r')
colors = [cmap(i) for i in np.linspace(0, 1, 7)]
colors1 = [(r, g, b, 0.7) for r, g, b, _ in colors]
colors2 = [(r, g, b, 1) for r, g, b, _ in colors]
all_colors = []
for i in range(len(colors1)):
    all_colors.extend([colors1[i], colors2[i]])
group_gap = 2
positions = []
for i in range(7):
    positions.extend([i * (2 + group_gap), i * (2 + group_gap) + 1])
plt.rc('font', family='Times New Roman', size=12)
fig, ax = plt.subplots(figsize=(4, 2), dpi=300)
bp = ax.boxplot(all_grouped_data, patch_artist=True, positions=positions)
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(all_colors[i])
# ax.set_ylabel('NSE')
ax.set_title('Year/Flood Corr')
ax.set_xticks([pos for i, pos in enumerate(positions) if i % 2 == 0])
ax.set_xticklabels(region_abbr)
ax.set_xlim(-1, positions[-1] + 1)
# legend_patches = [plt.Rectangle((0, 0), 1, 1, color=colors1[0], alpha=0.7),
#                   plt.Rectangle((0, 0), 1, 1, color=colors2[0], alpha=1)]
# ax.legend(legend_patches, ['Year', 'Flood'], loc='lower center', ncol=2,frameon=False)
plt.ylim([0.7,1])

plt.show()


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data1 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-1\第一轮7.xlsx')
regions = ["东北", "西北", "华北", "华东", "华中", "华南", "西南"]
region_abbr = ["NEC", "NWC", "NC", "EC", "CC", "SC", "SWC"]
grouped_data1 = [data1[data1['region'] == region]['test_corr'] for region in regions]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap(i) for i in np.linspace(0, 1, 7)]
colors1 = [(r, g, b, 0.8) for r, g, b, _ in colors]  # 统一透明度
positions = [i * 2 for i in range(len(grouped_data1))]
plt.rc('font', family='Times New Roman', size=12)
fig, ax = plt.subplots(figsize=(4, 2), dpi=300)
bp = ax.boxplot(grouped_data1, patch_artist=True, positions=positions)
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(colors1[i])
# ax.set_title('Year Precipitation Corr')
ax.set_xticks(positions)
ax.set_xticklabels(region_abbr)
ax.set_xlim(-1, positions[-1] + 1)
plt.ylim([0.70, 1])
plt.ylabel('R')
plt.show()


# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data1 = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-2\第一轮2.xlsx')
regions = ["东北", "西北", "华北", "华东", "华中", "华南", "西南"]
region_abbr = ["NEC", "NWC", "NC", "EC", "CC", "SC", "SWC"]
grouped_data1 = [data1[data1['region'] == region]['test_corr'] for region in regions]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap(i) for i in np.linspace(0, 1, 7)]
colors1 = [(r, g, b, 0.8) for r, g, b, _ in colors]  # 统一透明度
positions = [i * 2 for i in range(len(grouped_data1))]
plt.rc('font', family='Times New Roman', size=12)
fig, ax = plt.subplots(figsize=(4, 2), dpi=300)
bp = ax.boxplot(grouped_data1, patch_artist=True, positions=positions)
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(colors1[i])
# ax.set_title('Summer Precipitation Corr')
ax.set_xticks(positions)
ax.set_xticklabels(region_abbr)
ax.set_xlim(-1, positions[-1] + 1)
plt.ylim([0.70, 1])
plt.ylabel('R')
plt.show()


# In[ ]:





# In[2]:


import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
plt.rc('font', family='Times New Roman', size=10)
fig = plt.figure(figsize=(4, 2), dpi=300)
left, bottom, width, height = 0.1, 0.1, 1, 1
ax = fig.add_axes([left, bottom, width, height])
data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\china3.shp")
data.plot(ax=ax, facecolor='whitesmoke', edgecolor='gray', linewidth=0.5)
station_data = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model\第一轮3.xlsx')
cf = ax.scatter(station_data['lon'], station_data['lat'], c=station_data['test_corr'], s=5, cmap='RdBu_r', vmax=1, vmin=0)
cbar = plt.colorbar(cf, pad=0.03)
cbar.set_label('Corr')  
plt.ylim([15,55])
plt.xlim([70,138])
xticks = range(75, 140, 10)  
plt.xticks(xticks, [f'{x}°E' for x in xticks] , fontsize=10)
yticks = range(15, 60, 10)  
plt.yticks(yticks, [f'{y}°N' for y in yticks], fontsize=10)
ax2_left, ax2_bottom, ax2_width, ax2_height = 0.24, 0.15, 0.18, 0.2
ax2 = fig.add_axes([ax2_left, ax2_bottom, ax2_width, ax2_height])
intervals = [0, 0.1, 0.2, 0.3,0.4,0.5,0.6, 0.7,0.8, 0.9,1.0]
counts = [((station_data['train_corr'] >= intervals[i]) & (station_data['train_corr'] < intervals[i+1])).sum() for i in range(len(intervals)-1)]
cmap = plt.get_cmap('RdBu_r') 
colors = [cmap((intervals[i] + intervals[i+1]) / 2) for i in range(len(intervals)-1)]
ax2.bar(range(len(counts)), counts, tick_label=[f'{intervals[i]}-{intervals[i+1]}' for i in range(len(intervals)-1)], color=colors,)
ax2.patch.set_alpha(0.2)  # 设置透明度
ax2.tick_params(axis='x', direction='in')
ax2.tick_params(axis='y', direction='in')
ax2.set_xticklabels([])
ax2.set_ylim([0,30])
ax2.set_xlim([0,10])
ax2.set_title('Number Statistics', y=0.80,size=6)
ax2.tick_params(axis='both', which='major', labelsize=6)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
plt.rc('font', family='Times New Roman', size=10)
fig = plt.figure(figsize=(4, 2), dpi=300)
left, bottom, width, height = 0.1, 0.1, 1, 1
ax = fig.add_axes([left, bottom, width, height])
data = gpd.read_file(r"C:\Users\xiaotian\Desktop\data\GIS\china3.shp")
data.plot(ax=ax, facecolor='whitesmoke', edgecolor='gray', linewidth=0.5)
station_data = pd.read_excel(r'C:\Users\xiaotian\Desktop\data\model-2\第一轮2.xlsx')
cf = ax.scatter(station_data['lon'], station_data['lat'], c=station_data['test'], s=5, cmap='RdBu_r', vmax=1, vmin=0)
cbar = plt.colorbar(cf, pad=0.03)
cbar.set_label('NSE')  
plt.ylim([15,55])
plt.xlim([70,136])
xticks = range(75, 140, 10)  
plt.xticks(xticks, [f'{x}°E' for x in xticks], fontsize=10)
yticks = range(15, 60, 10)  
plt.yticks(yticks, [f'{y}°N' for y in yticks], fontsize=10)
ax2_left, ax2_bottom, ax2_width, ax2_height =  0.24, 0.15, 0.18, 0.2
ax2 = fig.add_axes([ax2_left, ax2_bottom, ax2_width, ax2_height])
intervals = [0, 0.1, 0.2, 0.3,0.4,0.5,0.6, 0.7,0.8, 0.9,1.0]
counts = [((station_data['test'] >= intervals[i]) & (station_data['test'] < intervals[i+1])).sum() for i in range(len(intervals)-1)]
cmap = plt.get_cmap('RdBu_r')
colors = [cmap((intervals[i] + intervals[i+1]) / 2) for i in range(len(intervals)-1)]
ax2.bar(range(len(counts)), counts, tick_label=[f'{intervals[i]}-{intervals[i+1]}' for i in range(len(intervals)-1)], color=colors,)
ax2.patch.set_alpha(0.2)  # 设置透明度
ax2.tick_params(axis='x', direction='in')
ax2.tick_params(axis='y', direction='in')
ax2.set_xticklabels([])
ax2.set_ylim([0,30])
ax2.set_xlim([0,10])
ax2.set_title('Number Statistics', y=0.80,size=6)
ax2.tick_params(axis='both', which='major', labelsize=6)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.show()


# In[ ]:




