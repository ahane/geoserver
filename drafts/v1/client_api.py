from flask import Flask
app = Flask(__name__)

#load references to layer services
layers = {'BerlinNightlife': 'http://localhost:5001'}

@app.route('api/layers/')
def list_layers():
    '''returns a json object containing a uris to all availiable layers'''

@app.route('api/layers/<str: layer_name>/')
def layer_metadata(layer_name):
    '''- GET information about layer from layer uri
         *Features uri
         *happening_features uri
         *happenings uri
       - return rich haljson with availiable options
    '''
@app.route('api/layers/<str: layer_name>/features/')
def all_features(layer_name):
    ''' - call layer_metadata
        - look up features_uri
        - GET features from features_uri (on layer service)
        - return features
    '''

@app.route('api/layers/<str: layer_name>/happenings/')
def has_happenings(layer_name):
    ''' - call layer_metadata ()
        - see if happening_features and exists
        - if not return 400
        - else return happening_features and filter schema?
    '''
@app.route('api/layers/<str: layer_name>/happenings/from/<str: start_datetime>/to/<str: end_datetime'):
def happening_features(layer_name, start_datetime, end_datetime):
    ''' - save happening_features uri from has_happenings(layer_name), if not return 400
        - validate datetimes
        - GET happenings/start/end from happening_features (on layer service)
        - return features
    '''

@app.route('api/layers/api/layers/<str: layer_name>/happenings/<int: happening_id>'):
def happening_resource(layer_name, happening_id):
    '''- get happenings uri from has_happenings, if not return 400
       - request resource from happenings uri (happenings service)
       - return resource
    '''
