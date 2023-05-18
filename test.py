from PIL import Image
import numpy as np
import streamlit as st
import numpy as np
import folium
import geopandas as gpd
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_folium import st_folium
from utils import popupTable
import branca
import cv2
import pandas as pd
import rasterio
# from PIL import Image
import os
import geojson


# df = pd.read_csv('./static/report.csv')
# df = df.dropna(thresh=4)
df = pd.read_csv('./static/GeneratedReport - GeneratedReport.csv')

insights = ["Temperature", "Vegetation encroachment","Land Subsidence","Potential Fouling","Corrosion"]
for i in insights:
    df_temp = df[['latitude', 'longitude', i]]
    df_temp = df_temp.dropna(thresh=3)
    #df_temp = df_temp.loc[df_temp[i] == ]

    df_temp.to_csv('./static/{}.csv'.format(''.join(i)),index = False)
# print(df['Temperature'].unique())
# insights = ["Temperature", "Vegetation encroachment","Land Subsidence","Potential Fouling","Corrosion"]
# for i in insights:
#     df_temp = df[['latitude', 'longitude', i]]
#     df_temp = df_temp.loc[df_temp[i] == 1]


# im = Image.open('./static/ls_third.tif')
# im.save('./static/ls_third.png')
# print(im)


# img = Image.open('./static/ls_third.png')
# img = img.convert("RGBA")
# datas = img.getdata()
# newData = []
# for item in datas:
#     if item[0] == 0 and item[1] == 0 and item[2] == 0:
#         newData.append((0, 0, 0, 0))
#     else:
#         newData.append(item)
 
# img.putdata(newData)
# img.save('./static/ls_third.png', "PNG")
# datastring = './static/map_row.geojson'
# with open(datastring) as f:
#     gj = geojson.load(f)

# geo = gj['features'][0]['geometry']['coordinates'][0]
# #print(geo)
# print(len(geo))
# print(geo[:10])