# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:32:02 2020

@author: Anjali
"""

import requests
import folium
import pandas as pd
import time

url = 'http://voicecar.pythonanywhere.com'
df = pd.DataFrame()
rows = []
map=folium.Map(location=[1.349, 103.748], zoom_start=5)
fgam = folium.FeatureGroup(name='Adult Mozzies')
fglm = folium.FeatureGroup(name='Mozzi Larvae')
fgsw = folium.FeatureGroup(name='Still Water')
fgem = folium.FeatureGroup(name='Mozzi Eggs')
map.add_child(fgam)
map.add_child(fgem)
map.add_child(fglm)
map.add_child(fgsw)
map.add_child(folium.LayerControl())

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

###################################################################################################

type_dict = {'AdultMosquito':fgam,'MosquitoLarva':fglm,'MosquitoEggs':fgem,'other': fgsw}
def get_ftype(typeof):
    typeof2 = typeof.replace(' ','')
    if typeof2 in type_dict:
        return type_dict[typeof2]
    else: 
        return type_dict['other']

type_color_dict = {'AdultMosquito':'blue','MosquitoLarva':'green','MosquitoEggs':'orange','other': 'red'}
def get_color(typeof):
    typeof2 = typeof.replace(' ','')
    if typeof2 in type_color_dict:
        return type_color_dict[typeof2]
    else: 
        return type_color_dict['other']

def add_marker(lat,long,typeof):
    folium.Marker(location=[lat,long],popup=folium.Popup(typeof,parse_html=True),
   icon=folium.Icon(get_color(typeof))).add_to(get_ftype(typeof))
    
#%%
#code i run

while True:
    res = requests.get(url).text
    if res:
        lat,long,typeof = res.split(',')
        rows.append([lat,long,typeof])
        #REset voixe car page
        requests.get(url+'/?key=')
        add_marker(lat,long,typeof)
    else:
        print('waiting for coordinates')
        pass
    map.save('Map.html')
    time.sleep(3)
        
###############################################################################
df = pd.concat([pd.DataFrame(rows, columns = ['lat','long']),df])

