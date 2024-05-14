import os
import pandas as pd
from pandas.api.types import CategoricalDtype

raw_data_path = './raw_data_test/'  # Path to raw data stored locally
gmd_data_path = './data/aq_data_test/'  # Path to groomed data

AQI_category = CategoricalDtype(categories=["Good", "Moderate", "Unhealthy for Sensitive Groups", 
                                            "Unhealthy", "Very Unhealthy", "Hazardous"], ordered=True)
PM25_Category = CategoricalDtype(categories=["< 12.00", "12.00 - 35.50", "35.50 - 85.50", 
                                                "115.00 - 150.50", "150.50+"], ordered=True)
MesoWest_Category = CategoricalDtype(categories=['< 2.00', '2.00 - 4.00', '4.00 - 6.00', 
                                                    '6.00 - 8.00', '8.00 - 10.00','10.00 - 12.00',
                                                    '12.00 - 20.00','20.00 - 28.00','28.00 - 35.50',
                                                    '35.50 - 45.50','45.50 - 55.50','55.50 - 85.50',
                                                    '85.50 - 115.50','115.50 - 150.50','150.50+'], ordered=True)

for filename in os.listdir(raw_data_path):
    if filename.endswith('.csv'):
        raw_file_path = os.path.join(raw_data_path, filename)
        gmd_file_path = os.path.join(gmd_data_path, filename)
        transit_id = filename.split('_')[0]
        transit_df = pd.read_csv(raw_file_path, low_memory=False)

        headers = transit_df.columns.to_list()
        units = transit_df.iloc[0].to_list()

        new_headers = [f'{h}_{u}' for h, u in zip(headers, units)]

        transit_df = transit_df.iloc[1:].reset_index(drop=True)
        transit_df.columns = pd.Index(new_headers)
        transit_df['Timestamp_UTC'] = pd.to_datetime(
            transit_df['Timestamp_UTC'])
        transit_df.iloc[:, 1:-2] = transit_df.iloc[:, 1:-2].astype(float)

        transit_df['Time_Tuple'] = transit_df['Timestamp_UTC'].apply(
            lambda x: x.timetuple())
        transit_df['Date'] = transit_df['Timestamp_UTC'].apply(
            lambda x: x.date())
        transit_df['Year'] = transit_df['Timestamp_UTC'].apply(
            lambda x: x.timetuple().tm_year)
        transit_df['Month'] = transit_df['Timestamp_UTC'].apply(
            lambda x: x.timetuple().tm_mon)
        transit_df['Day_of_Year'] = transit_df['Timestamp_UTC'].apply(
            lambda x: x.timetuple().tm_yday)
        transit_df['Day_of_Month'] = transit_df['Timestamp_UTC'].apply(
            lambda x: x.timetuple().tm_mday)
        transit_df['Minute'] = transit_df['Timestamp_UTC'].apply(
            lambda x: x.timetuple().tm_min)
        transit_df['Hour'] = transit_df['Timestamp_UTC'].apply(
            lambda x: x.timetuple().tm_hour)
        transit_df['Transit_ID'] = transit_id
        
        pm25_cols = transit_df.filter(like='PM2.5_Concentration_ug/m3')
        ozone_cols = transit_df.filter(like='Ozone_Concentration_ppbv')
        
        transit_df['AQI'] = pm25_cols.apply(lambda x: 'Good' if x < 12
                                            else ('Moderate' if x < 35.5
                                                  else ('Unhealthy for Sensitive Groups' if x < 55.5
                                                        else ('Unhealthy' if x < 150.5
                                                              else ('Very Unhealthy' if x < 250.5 else 'Hazardous')))))

        transit_df['PM2.5_Category'] = pm25_cols.apply(lambda x: '< 12.00' if x < 12.00
                                                       else ('12.00 - 35.50' if x < 35.50
                                                             else ('35.50 - 85.50' if x < 85.50
                                                                else ('115.00 - 150.50') if x < 150.50
                                                                else ('150.50+'))))


        transit_df['Meso_West_Category'] = pm25_cols.apply(lambda x: '< 2.00' if x < 2.00
                                                           else ('2.00 - 4.00' if x < 4.00
                                                                 else ('4.00 - 6.00' if x < 6.00
                                                                      else ('6.00 - 8.00') if x < 8.00
                                                                      else ('8.00 - 10.00') if x < 10.00
                                                                      else ('10.00 - 12.00') if x < 12.00
                                                                      else ('12.00 - 20.00') if x < 20.00
                                                                      else ('20.00 - 28.00') if x < 28.00
                                                                      else ('28.00 - 35.50') if x < 35.50
                                                                      else ('35.50 - 45.50') if x < 45.50
                                                                      else ('45.50 - 55.50') if x < 55.50
                                                                      else ('55.50 - 85.50') if x < 85.50
                                                                      else ('85.50 - 115.50') if x < 115.50
                                                                      else ('115.50 - 150.50') if x < 150.50
                                                                      else ('150.50+'))))

        transit_df['AQI'] = transit_df['AQI'].astype(AQI_category)
        transit_df['PM2.5_Category'] = transit_df['PM2.5_Category'].astype(PM25_Category)
        transit_df['Meso_West_Category'] = transit_df['Meso_West_Category'].astype(MesoWest_Category)

        transit_df_filt = transit_df[
            (pm25_cols != -9999.00).all(axis=1) &
            (ozone_cols != -9999.00).all(axis=1) &
            (transit_df['Latitude_ddeg'] != -9999.00) &
            (transit_df['Longitude_ddeg'] != -9999.00)]

        transit_df_gmd = transit_df_filt.iloc[::30, :].reset_index(drop=True)
        transit_df_gmd.to_csv(gmd_file_path, index=False)
        print(f'Groomed: {filename}')
