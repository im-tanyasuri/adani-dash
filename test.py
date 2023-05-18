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


im = Image.open('./static/temp_row.tif')
im.save('./static/temp_row.png')
print(im)


img = Image.open('./static/temp_row.png')
img = img.convert("RGBA")
datas = img.getdata()
newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((0, 0, 0, 0))
    else:
        newData.append(item)
 
img.putdata(newData)
img.save('./static/temp_row.png', "PNG")
# datastring = './static/map_row.geojson'
# with open(datastring) as f:
#     gj = geojson.load(f)

# geo = gj['features'][0]['geometry']['coordinates'][0]
# #print(geo)
# print(len(geo))
# print(geo[:10])