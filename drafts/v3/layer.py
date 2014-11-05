from hinterteil import Hinterteil
from haleluja import HalBuilder
from pandas import DataFrame
from flask import Flask, json, url_for, request


app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5001'
app.config['LAYER_URLS'] = [('berlin-nightlife', 'http://localhost:5000/api/')]

layer_servers = {name: Hinterteil(url) for name, url in app.config['LAYER_URLS']}
curie_pref = 'raumzeit:'

@app.route('/')
def index():
    self_href = request.base_url
    builder = HalBuilder(self_href)
    builder.add_link('latest-version', url_for('curr_version'))
    return json.jsonify(builder.as_object())

@app.route('/v1/')
def curr_version():
    self_href = request.base_url
    builder = HalBuilder(self_href)

    layers_rel = curie_pref + 'layers'
    layers_url = url_for('layers')
    builder.add_link(layers_rel, layers_url)

    return json.jsonify(builder.as_object())


@app.route('/v1/layers/')
def layers():
    self_href = request.base_url
    builder = HalBuilder(self_href)

    layer_rel = curie_pref + 'layer'
    for l in layer_servers.keys():
        layer_url = url_for('layer', layer_name=l)
        builder.add_link(layer_rel, layer_url)

    return json.jsonify(builder.as_object())

@app.route('/v1/layers/<layer_name>')
def layer(layer_name):
    self_href = request.base_url
    builder = HalBuilder(self_href)

    features_rel = curie_pref + 'features'
    features_url = request.url_root.rstrip('/') + url_for('features', layer_name=layer_name)
    builder.add_link(features_rel, features_url)

    return json.jsonify(builder.as_object())

@app.route('/v1/layers/<layer_name>/features/')
def features(layer_name):
 # translates the query args for the hinterteil
    self_href = request.base_url
    builder = HalBuilder(self_href)

    syn = {'features': 'venue'}
    layer_server = layer_servers[layer_name]

    features_table = syn['features']
    df = layer_server.get_df(features_table)

    # Add new url
    root_url = request.base_url
    df['front_url'] = root_url + df['id'].apply(str)

    # Add link to happenings
    happ_rel = curie_pref + 'happenings'
    df[happ_rel] = df['front_url'] + '/happenings/'

    rel = curie_pref + 'feature'
    builder.embed_df(df, 'front_url', rel, ['name', 'lat', 'lon'], [happ_rel])

    return json.jsonify(builder.as_object())

def filter_by_happenings(features_key, happenings_key, after, before):
    '''
    Returns a DataFrame of features which have happenings in a given time frame.

    :param features_key: The name of the features column the happenings table
    :param happenings_key: The name of the happenings table.
    :param after:A iso formatted string denoting the start of our time frame
    :param before: A iso formatted string denoting the end of our time frame.
    :return: `DataFrame` with features.
    '''
    query = {'filters': [
        {'name': 'start_datetime', 'op': '>=', 'val': after}

    ]}

    events =


@app.route('/v1/layers/<layer_name>/features/<feature_id>')
def feature(layer_name, feature_id):
    # self_href = request.base_url
    # builder = HalBuilder(self_href)
    #
    # layer_dict = {'features': 'venue', 'happenings': 'event'}
    # layer_server = layer_servers[layer_name]
    #
    # df = layer_server.get_df(layer_dict['happenings'])
    # root_url = request.base_url
    # df['url'] = root_url + df['id'].apply(str)
    # rel = curie_pref + 'feature'
    # builder.embed_df(df, 'url', rel, ['name', 'lat', 'lon'])
    return 'Not yet implemented'

@app.route('/v1/layers/<layer_name>/features/<feature_id>/happenings/')
def happenings(layer_name, feature_id):
    self_href = request.base_url
    builder = HalBuilder(self_href)

    syn = {'features': 'venue', 'happenings': 'events'}
    layer_server = layer_servers[layer_name]

    feature_df = layer_server.get_df(syn['features'], item_id=feature_id)
    happings_col = syn['happenings']
    happenings_df = feature_df[happings_col][0] # we select the first and only row

    # Add new url
    root_url = request.base_url
    happenings_df['front_url'] = root_url + happenings_df['id'].apply(str)

    rel = curie_pref + 'happening'
    builder.embed_df(happenings_df, 'front_url', rel, ['start_datetime', 'end_datetime', 'name'])

    return json.jsonify(builder.as_object())



if __name__ == '__main__':
    app.run(port=5001, debug=True)