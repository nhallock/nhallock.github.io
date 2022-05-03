#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import geopandas as gpd
import folium


# In[19]:


# Read in Bull Trout Data and Filter for 0% Brook Trout invasion
# 1980
BullTrout1980 = gpd.read_file('S_USA.ClimateShield_BULL0BRK0_1980.gdb.zip')
BullTrout1980["geoid"] = BullTrout1980.index.astype(str)
BullTrout1980 = BullTrout1980[["geoid", "BT_0BRK", "geometry"]]

# 2040
BullTrout2040 = gpd.read_file('S_USA.ClimateShield_BULL0BRK0_2040.zip')
BullTrout2040["geoid"] = BullTrout2040.index.astype(str)
BullTrout2040 = BullTrout2040[["geoid", "BT_0BRK", "geometry"]]

# 2080
BullTrout2080 = gpd.read_file('S_USA.ClimateShield_BULL0BRK0_2080.gdb.zip')
BullTrout2080["geoid"] = BullTrout2080.index.astype(str)
BullTrout2080 = BullTrout2080[["geoid", "BT_0BRK", "geometry"]]
BullTrout2080



# In[20]:


# Create our folium map to add Bull Trout data to
center = (46.265294, -117.742468)
bullTroutMap = folium.Map(location = center, width = 500, height = 500, 
                        zoom_start=5, min_zoom=5,
                        min_lat= 32, 
                        max_lat=  55, 
                        min_lon=-134, 
                        max_lon= -96,
                        max_bounds=True,
                        tiles = 'Stamen Terrain')

# Create the 1980 Bull Trout population layer
BullTrout1980Layer = folium.Choropleth(BullTrout1980,
                                      data=BullTrout1980,
                                      columns=['geoid','BT_0BRK'],  
                                      key_on='feature.id', 
                                      line_opacity=1,
                                      line_color='green',
                                      name = 'Bull Trout 1980',
                                      highlight=True,
                                      overlay=True,)

# remove the legend as it is not useful in this instance
for key in BullTrout1980Layer._children:
    if key.startswith('color_map'):
        del(BullTrout1980Layer._children[key])

# Create the 2040 Bull Trout population layer
BullTrout2040Layer = folium.Choropleth(BullTrout2040,
                                      data=BullTrout2040,
                                      columns=['geoid','BT_0BRK'],  
                                      key_on='feature.id', 
                                      line_opacity=1,
                                      line_color='yellow',
                                      name = 'Bull Trout 2040',
                                      highlight=True,
                                      overlay=True,)

# remove the legend as it is not useful in this instance
for key in BullTrout2040Layer._children:
    if key.startswith('color_map'):
        del(BullTrout2040Layer._children[key])

# Create the 1980 Bull Trout population layer
BullTrout2080Layer = folium.Choropleth(BullTrout2080,
                                      data=BullTrout2080,
                                      columns=['geoid','BT_0BRK'],  
                                      key_on='feature.id', 
                                      line_opacity=1,
                                      line_color='red',
                                      name = 'Bull Trout 2080',
                                      highlight=True,
                                      overlay=True,)

# remove the legend as it is not useful in this instance
for key in BullTrout2080Layer._children:
    if key.startswith('color_map'):
        del(BullTrout2080Layer._children[key])

# Add our choropleth layers to the map 
BullTrout1980Layer.add_to(bullTroutMap)
BullTrout2040Layer.add_to(bullTroutMap)
BullTrout2080Layer.add_to(bullTroutMap)

# Add layer control to our map to be able to turn layers on and off
folium.LayerControl().add_to(bullTroutMap)

# Display our Bull Trout map
bullTroutMap


# In[21]:


bullTroutMap.save('BT_0BRK.html')


# In[42]:


# Read in Cutthroat Trout Data and Filter for 0% Brook Trout invasion
# 1980
CutTrout1980 = gpd.read_file('S_USA.ClimateShield_CT0BRK0_1980.gdb.zip')
CutTrout1980["geoid"] = CutTrout1980.index.astype(str)
CutTrout1980 = CutTrout1980[["geoid", "CT_0BRK", "geometry"]]

n = len(CutTrout1980)
CutTrout1980 = CutTrout1980.drop(range(5000, n))

# 2040
CutTrout2040 = gpd.read_file('S_USA.ClimateShield_CT0BRK0_2040.gdb.zip')
CutTrout2040["geoid"] = CutTrout2040.index.astype(str)
CutTrout2040 = CutTrout2040[["geoid", "CT_0BRK", "geometry"]]

n = len(CutTrout2040)
CutTrout1980 = CutTrout2040.drop(range(5000, n))

# 2080
CutTrout2080 = gpd.read_file('S_USA.ClimateShield_CT0BRK0_2080.gdb.zip')
CutTrout2080["geoid"] = CutTrout2080.index.astype(str)
CutTrout2080 = CutTrout2080[["geoid", "CT_0BRK", "geometry"]]

n = len(CutTrout2080)
CutTrout1980 = CutTrout2080.drop(range(5000, n))


# In[43]:


# Create our folium map to add Cutthroat Trout data to
center = (46.265294, -117.742468)
CutTroutMap = folium.Map(location = center, width = 500, height = 500, 
                        zoom_start=5, min_zoom=5,
                        min_lat= 32, 
                        max_lat=  55, 
                        min_lon=-134, 
                        max_lon= -96,
                        max_bounds=True,
                        tiles = 'Stamen Terrain')

# Create the 1980 Cutthroat Trout population layer
CutTrout1980Layer = folium.Choropleth(CutTrout1980,
                                      data=CutTrout1980,
                                      columns=['geoid','CT_0BRK'],  
                                      key_on='feature.id', 
                                      line_opacity=1,
                                      line_color='green',
                                      name = 'Cut Trout 1980',
                                      highlight=True,
                                      overlay=True,)

# remove the legend as it is not useful in this instance
for key in CutTrout1980Layer._children:
    if key.startswith('color_map'):
        del(CutTrout1980Layer._children[key])

# Create the 2040 Cutthroat Trout population layer
CutTrout2040Layer = folium.Choropleth(CutTrout2040,
                                      data=CutTrout2040,
                                      columns=['geoid','CT_0BRK'],  
                                      key_on='feature.id', 
                                      line_opacity=1,
                                      line_color='yellow',
                                      name = 'Cut Trout 2040',
                                      highlight=True,
                                      overlay=True,)

# remove the legend as it is not useful in this instance
for key in CutTrout2040Layer._children:
    if key.startswith('color_map'):
        del(CutTrout2040Layer._children[key])

# Create the 2080 Cutthroat Trout population layer
CutTrout2080Layer = folium.Choropleth(CutTrout2080,
                                      data=CutTrout2080,
                                      columns=['geoid','CT_0BRK'],  
                                      key_on='feature.id', 
                                      line_opacity=1,
                                      line_color='red',
                                      name = 'Cut Trout 2080',
                                      highlight=True,
                                      overlay=True,)

# remove the legend as it is not useful in this instance
for key in CutTrout2080Layer._children:
    if key.startswith('color_map'):
        del(CutTrout2080Layer._children[key])

# Add our choropleth layers to the map 
CutTrout1980Layer.add_to(CutTroutMap)
CutTrout2040Layer.add_to(CutTroutMap)
CutTrout2080Layer.add_to(CutTroutMap)

# Add layer control to our map to be able to turn layers on and off
folium.LayerControl().add_to(CutTroutMap)

# Display our Cutthroat Trout map
CutTroutMap


# In[44]:


CutTroutMap.save('CT_0BRK.html')


# In[45]:


get_ipython().system('jupyter nbconvert --to script flyAway.ipynb')

