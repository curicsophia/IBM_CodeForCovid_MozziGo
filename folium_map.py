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

def set_up(df):
    def add_marker(lat,long,typeof):
        folium.Marker(location=[lat,long],popup=folium.Popup(typeof,parse_html=True),
            icon=folium.Icon(get_color(typeof)))\
                      .add_to(get_ftype(typeof))
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    def get_ftype(typeof):
        typeof2 = typeof.replace(' ','')
        if typeof2 in type_dict:
            return type_dict[typeof2]
        else: 
            return type_dict['other']
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_color(typeof):
        typeof2 = typeof.replace(' ','')
        if typeof2 in type_color_dict:
            return type_color_dict[typeof2]
        else: 
            return type_color_dict['other']

    # Singapore
    #map=folium.Map(location=[1.349, 103.748], zoom_start=5)
    
    fmap=folium.Map(location=[1.349, 103.748], zoom_start= 12)
    fgam = folium.FeatureGroup(name='Adult Mozzies')
    fglm = folium.FeatureGroup(name='Mozzi Larvae')
    fgsw = folium.FeatureGroup(name='Still Water')
    fgem = folium.FeatureGroup(name='Mozzi Eggs')
    fmap.add_child(fgam)
    fmap.add_child(fgem)
    fmap.add_child(fglm)
    fmap.add_child(fgsw)
    fmap.add_child(folium.LayerControl())
    
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
    
    fmap.get_root().html.add_child(folium.Element(legend_html))
    type_dict = {'AdultMosquito':fgam,'MosquitoLarva':fglm,'MosquitoEggs':fgem,'other': fgsw}
    type_color_dict = {'AdultMosquito':'blue','MosquitoLarva':'green','MosquitoEggs':'orange','other': 'red'}
    for row in df.itertuples():
        add_marker(row.lat,row.long,row.typeof)    
    fmap.save('Map.html')

###################################################################################################

def get_ftype(type_dict,typeof):
    typeof2 = typeof.replace(' ','')
    if typeof2 in type_dict:
        return type_dict[typeof2]
    else: 
        return type_dict['other']

def get_color(type_color_dict,typeof):
    typeof2 = typeof.replace(' ','')
    if typeof2 in type_color_dict:
        return type_color_dict[typeof2]
    else: 
        return type_color_dict['other']

def add_marker(fmap, type_dict, type_color_dict, lat,long,typeof):
    folium.Marker(location=[lat,long],popup=folium.Popup(typeof,parse_html=True),
        icon=folium.Icon(get_color(type_color_dict, typeof)))\
                  .add_to(get_ftype(type_dict, typeof))
    return fmap
    
def record_point(lat,long,typeof):
    # read points csv
    # good save new points to csv file
    #point_csv = pd.DataFrame([[4,3,'other']], columns = columns)
    filename = 'test_points.csv'
    point_save = ','.join([str(e) for e in [lat,long,typeof]]) +'\n'
    with open(filename,'a+') as f:
        f.write(point_save)
    
def save_map():
    # read points csv
    # create map and cotrol points
    fmap, type_dict, type_color_dict = set_up()
    # create point for each point in csv
    # save map to file
    filename = 'test_points.csv'
    columns = ['lat','long','typeof']
    df_load = pd.read_csv(filename, header= None)
    df_load.columns = columns  
    rows = df.to_dict(orient = 'records')
    for d in rows:
        fmap = add_marker(fmap, type_dict, type_color_dict,
                          d['lat'],d['long'],d['typeof'])
    fmap.save('Map.html')
    
    
#%%
#code i run

if False:
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
        

# %%
        
if True:
    while True:
        res = requests.get(url).text
        if res:
            # record poinr
            lat,long,typeof = res.split(',')
            record_point(lat,long,typeof)
            requests.get(url+'/?key=')
            # save map
            filename = 'test_points.csv'
            columns = ['lat','long','typeof']
            df_load = pd.read_csv(filename, header= None)
            df_load.columns = columns  
            set_up(df_load)
        else:
            print('waiting for coordinates')
        time.sleep(3)
        
# %%

if False:        
    try:
        filename = 'test_points.csv'
        columns = ['lat','long','typeof']
        df_load = pd.read_csv(filename, header= None)
        df_load.columns = columns  
    except Exception as e:
        df_load = pd.DataFrame()
    set_up(df_load)

# %%

filename = 'test_points.csv'
with open(filename,'w') as f:
    f.truncate(0)
    
    

    