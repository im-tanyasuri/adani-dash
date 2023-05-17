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



im = Image.open('./static/4_corr.tif')
im.save('./static/4_corr.png')
print(im)


img = Image.open('./static/4_corr.png')
img = img.convert("RGBA")
datas = img.getdata()
newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((0, 0, 0, 0))
    else:
        newData.append(item)
 
img.putdata(newData)
img.save('./static/4_corr.png', "PNG")
