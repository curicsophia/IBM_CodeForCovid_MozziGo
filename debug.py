# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:00:29 2020

@author: Anjali
"""

# %%
import pandas as pd

df1 = pd.DataFrame([1,2,3])
df2 = pd.DataFrame([10,12,4])

df= pd.concat([df1,df2])

# %%

from folium.plugins import MarkerCluster

mc = MarkerCluster()
#creating a Marker for each point in df_sample. Each point will get a popup with their zip
for row in subset_of_df.itertuples():
    mc.add_child(folium.Marker(location=[row.INTPTLAT,  row.INTPTLONG],
                 popup=row.GEOID))
# %%

legend_html =   '''
                <div style="position: fixed; 
                            background-color: white;
                            bottom: 50px; left: 50px; width: 180px; height: 300px; 
                            border:2px solid grey; z-index:9999; font-size:14px;
                            ">
                            <br> &nbsp;<b> Legend</b> <br>
                              <tr><td> &nbsp; Adult Mozzi </td><td> <i class="fa fa-map-marker fa-2x" style="color:blue"></i></td></tr>
                              <tr><td>&nbsp; Mozzi Larvae &nbsp; </td><td><i class="fa fa-map-marker fa-2x" style="color:green"></i></td></tr>
                              <tr><td>&nbsp; Mozzi Eggs &nbsp; </td><td><i class="fa fa-map-marker fa-2x" style="color:orange"></i></td></tr>
                              <tr><td>&nbsp; Still Water &nbsp; </td><td><i class="fa fa-map-marker fa-2x" style="color:red"></i></td></tr>
                              </table>
                </div>
                ''' 

map.get_root().html.add_child(folium.Element(legend_html))

# %%

import folium

map=folium.Map(location=[1.349, 103.748], zoom_start=5)
fgam = folium.FeatureGroup(name='Adult Mozzies')
map.add_child(fgam)
map.add_child(folium.LayerControl())

type_color_dict = {'AdultMosquito':'red','MosquitoLarva':'green','MosquitoEggs':'orange','other': 'red'}
def get_color(typeof):
    typeof2 = typeof.replace(' ','')
    if typeof2 in type_color_dict:
        return type_color_dict[typeof2]
    else: 
        return type_color_dict['other']
    
type_dict = {'AdultMosquito':fgam,'MosquitoLarva':fglm,'MosquitoEggs':fgem,'other': fgsw}
def get_ftype(typeof):
    typeof2 = typeof.replace(' ','')
    if typeof2 in type_dict:
        return type_dict[typeof2]
    else: 
        return type_dict['other']

lat = 0
long = 1
typeof = 'AdultMosquito'
folium.Marker(location=[lat,long],popup=folium.Popup(typeof,parse_html=True),
   icon=folium.Icon(get_color(typeof))).add_to(get_ftype(typeof))


legend_html =   '''
                <div style="position: fixed; 
                            background-color: white;
                            bottom: 50px; left: 50px; width: 180px; height: 300px; 
                            border:2px solid grey; z-index:9999; font-size:14px;
                            ">
                            <br> &nbsp;<b> Legend</b> <br>
                            <table style="width:100%">
                              <tr><td> &nbsp; Adult Mozzi </td><td> <i class="fa fa-map-marker fa-2x" style="color:blue"></i></td></tr>
                              <tr><td>&nbsp; Mozzi Larvae &nbsp; </td><td><i class="fa fa-map-marker fa-2x" style="color:green"></i></td></tr>
                              <tr><td>&nbsp; Mozzi Eggs &nbsp; </td><td><i class="fa fa-map-marker fa-2x" style="color:orange"></i></td></tr>
                              <tr><td>&nbsp; Still Water &nbsp; </td><td><i class="fa fa-map-marker fa-2x" style="color:red"></i></td></tr>
                              </table>
                </div>
                ''' 

map.get_root().html.add_child(folium.Element(legend_html))

#folium.Marker(location=[lat,long]).add_to(fgam)
map.save('Map.html')
