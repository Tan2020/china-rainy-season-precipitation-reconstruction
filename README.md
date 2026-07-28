China Rainy-Season Precipitation Reconstruction Dataset over the Past 500 Years—CRP Dataset Documentation
1. Dataset Overview 
This dataset provides continuous reconstructed rainy-season precipitation series for China from 1470 to 2022, covering 92 stations nationwide. The dataset was developed from high-quality historical drought–flood grade data and modern precipitation observations using station-scale nonlinear temporal models based on LSTM. Compared with traditional static mapping or linear statistical methods, this dataset substantially improves the temporal consistency and spatial stability of historical precipitation reconstruction, as well as the ability to identify extreme events. The data are provided in both NetCDF format with a station dimension and Excel format, facilitating their use in studies of climate change, hydrology, and extreme events. The dataset is intended to provide fundamental data for studies of hydroclimatic change, wet–dry evolution, extreme drought events, and modern precipitation anomalies within a historical context in China over the past 500 years.
2. Data Content and File Structure
The dataset contains the following files:
(1) CRP_Dataset_station_data.nc
Format: NetCDF
Structure:
Dimensions: time (1470–2022) and station (92 stations)
Variables:
CRP(time, station): rainy-season precipitation, mm
lat(station): latitude
lon(station): longitude
Missing values: NaN
Features: Suitable for climate analysis, visualization, spatiotemporal statistics, and model-driven studies.
(2) CRP_Dataset.xlsx
Content: Annual reconstructed rainy-season precipitation data for each station from 1470 to 2022.
Purpose: Facilitates rapid data browsing, data import, and basic analysis.
(3) station.xlsx
Content: Station names, latitude and longitude, climatic regions, and start and end years.
