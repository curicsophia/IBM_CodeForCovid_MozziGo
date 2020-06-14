from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json

# Our imports
import requests
import folium
import pandas as pd
#import time

# %%

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
    fmap=folium.Map(location=[1.349, 103.748], zoom_start=12)
    
    #fmap=folium.Map(location=[0, 0], zoom_start= 4)
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
    fmap.save('templates/Map.html')

def record_point(lat,long,typeof):
    # read points csv
    # good save new points to csv file
    #point_csv = pd.DataFrame([[4,3,'other']], columns = columns)
    filename = 'test_points.csv'
    point_save = ','.join([str(e) for e in [lat,long,typeof]]) +'\n'
    with open(filename,'a+') as f:
        f.write(point_save)



# %%
# Bolierplate code

app = Flask(__name__, static_url_path='')

db_name = 'mydb'
client = None
db = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif "CLOUDANT_URL" in os.environ:
    client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'], url=os.environ['CLOUDANT_URL'], connect=True)
    db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route('/')
def root():
    return app.send_static_file('index.html')

# /* Endpoint to greet and add a new visitor to database.
# * Send a POST request to localhost:8000/api/visitors with body
# * {
# *     "name": "Bob"
# * }
# */
@app.route('/api/visitors', methods=['GET'])
def get_visitor():
    if client:
        return jsonify(list(map(lambda doc: doc['name'], db)))
    else:
        print('No database')
        return jsonify([])

# /**
#  * Endpoint to get a JSON array of all the visitors in the database
#  * REST API example:
#  * <code>
#  * GET http://localhost:8000/api/visitors
#  * </code>
#  *
#  * Response:
#  * [ "Bob", "Jane" ]
#  * @return An array of all the visitor names
#  */
@app.route('/api/visitors', methods=['POST'])
def put_visitor():
    user = request.json['name']
    data = {'name':user}
    if client:
        my_document = db.create_document(data)
        data['_id'] = my_document['_id']
        return jsonify(data)
    else:
        print('No database')
        return jsonify(data)

@app.route('/point', methods=['GET', 'POST'])
def point():
    message = ''
    try:
        res = request.args.get('key')
        if res:
            message += 'key=|%s|' % str(res)
            try:
                lat,long,typeof = res.split(',')
                lat =float(lat)
                long = float(long)
                record_point(lat, long, typeof)
                return '%s, Successfuly added: %s' % (message,res)            
            except Exception as e:
                return '%s, Invalid argument %s, ERROR: %s' % (message,res,e)
        else:
            return '%s, Expected lat,long,typeof' % message
    except Exception as e:
        print('%s : %s' % (message, e))
        
@app.route('/reset')
def reset():
    filename = 'test_points.csv'
    with open(filename,'w') as f:
        f.truncate(0)
    df_load = pd.DataFrame()
    set_up(df_load)
    return render_template("Map.html")
    
@app.route('/map')
def graph():
    # generate map
    try:
        filename = 'test_points.csv'
        columns = ['lat','long','typeof']
        df_load = pd.read_csv(filename, header= None)
        df_load.columns = columns  
    except Exception as e:
        df_load = pd.DataFrame()
    set_up(df_load)
    return render_template("Map.html")

@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
