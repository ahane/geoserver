from flask import Flask
app = Flask(__name__)

#CONFIG
DB = 'http://localhost:6000/'
FEATURES_EXT = 'venues/'
FEATURE_SCHEMA = 'something that defines what to include in a feature from the db'
HAPPENINGS_SERVICE = 'http://localhost:7000/'


@app.route('/')
def describe_layer():
    '''- return name, links to features, happening_features, happenings'''

@app.route('features/')
def geo_json_features():
    ''' - features()
        - return geojson(features)
    '''
@app.route('happenings_features/from/<str: start_datetime>/to/<str: end_datetime>')
    ''' features =  features()
        active_features = []
        for features in features:
            GET feature_db_uri, start, end from Happeings_service
            if 201:
                feature.happenings = response.happenings
                active_features.append(fature)
        return active_features
    '''
def geojson(features):
    ''' convert features into geojson FeatureCollection
    '''
def features():
    ''' _request_raw_features
        _apply_schema
        return schematized features
    '''

def _request_raw_features():
    ''' - request features from db
    '''
def _apply_schema(features):
    ''' - apply FEATURE_SCHEMA to results from db
    '''
