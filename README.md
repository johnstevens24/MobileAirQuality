# Mobile Air Quality Monitoring in the Salt Lake Valley

## COMP 5960: Applied Data Visualization Final Project -- Fall 2023

### Background & Motivation

The Salt Lake Valley (SLV) faces air quality challenges, especially in winter when temperature inversions trap pollutants, leading to PM2.5 exceedances for 18 days per winter. Summer sees elevated ground-level ozone for an average of 22 days annually. As an SLV resident, the health impacts of poor air quality, exacerbated on the West side with a higher proportion of minority residents, are concerning. Current awareness efforts lack accessible visuals for the general public. The University of Utah's Department of Atmospheric Sciences uses mobile air quality monitoring on public transit to provide local insights. This data is crucial for formulating effective policies to protect public health, especially considering the intersection of air quality with climate change. The goal of this project is to improve understanding and visualization of environmental impact, contributing to efforts to enhance air quality in the SLV.

### Data

Archived historical raw data (compressed CSV files) from research-grade pollutant sensors on 3 light-trail cars, traveling on the Red, Green, and Blue UTA TRAX lines in the SLV, have been provided by Drs. Alex Jacques and Daniel Mendoza, research scientists in the Department of Atmospheric Sciences at the University of Utah ([UTA TRAX](https://utahaq.chpc.utah.edu/aq/historical_archive/UTA_TRAX/); [UTA EBUS](https://utahaq.chpc.utah.edu/aq/historical_archive/UTA_EBUS/)). This dataset is part of an ongoing mobile air quality monitoring project called the TRAX Observation Project ([MesoWest Utah Air Quality Observations](https://utahaq.chpc.utah.edu/aq/cgi-bin/mobile_data.cgi)) and includes GPS positioning, train-top ambient temperature and humidity, PM2.5 measurements from a Met One ES-642 Dust Monitor, and ozone measurements from a 2B Technologies 205 Ozone Monitor. We may include archived historical raw data from 5 e-buses, traveling around in the SLV, and fixed-site platforms that contain PM2.5 measurements from Met One ES-642 Dust Monitors as well, but including all that data may be too much data to handle in this project timeline.

Socioeconomic demographic data, such as race and ethnicity distribution, household income, median household income, mean household income, per capita income, and median house value – all by zip code area within Utah, will be obtained from the [US Census Bureau](https://data.census.gov/). Cartographic boundary shapefiles of US zip code areas for plotting the zip code area geometries will also be gathered from the US Census Bureau ([TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)).