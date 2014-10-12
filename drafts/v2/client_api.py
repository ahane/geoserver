
LAYERS

@route('/')
def redirect_to_layers():

@route('/api/layers/')
def list_layers():
    ''' Returns a Collection+JSON containing layer items

        Pseudocode:
        -----------
        for layer_uri in LAYERS:
            GET layer metadata from layer_url

        compile layers into CJ items
        append profile link
        append version
        append self href

        return CJ
    '''

@route('api/layers/<layer_id>')
def layer_metadata(layer_id):
    ''' Returns a Collection+JSON containing layer meta data.

        Pseudocode:
        -----------
        look up layer_url via layer_id
        GET layer from layer_url
        substitute hrefs

        return CJ
    '''

@route('api/layers/<layer_id>/features/)
def features(layer_id):
    ''' Returns a Collection+JSON containing all features of a layer.

        Pseudocode:
        -----------
        if has query `joined_resource`:
            return features_joined(layer_id, joined_resource, query)
        else:
        call layer_metadata(layer_id)
        extract features_url
        GET features from features_url
        for each feature:
            substitute hrefs

        return CJ
    '''


def features_joined(layer_id, joined_resource, query):
    ''' Returns a Collection+JSON containing features.
        Features carry links to a joined resource.
        Should be combined with a query on the joined table.

        Example: /features?joined_resource=happenings&after=2014-1-1&before=2014-1-2

        Pseudocode:
        -----------
        call layer_metadata(layer_id)
        if layer has query with name=`joined_resource` and rel = jn.net/join:
            GET query_uri query_params
            substitute hrefs
            return cj
        else
            reuturn BAD REQUEST
    '''

@route('api/layers/<layer_id>/features/<feature_id>)
def feature(layer_id, feature_id):
    ''' Returns Collection+JSON with single feature.
        Can be combined with query.

        features = []
        if has query:
            features = features_joined(layer_id, query)
        else:
            features = features(layer_id)
        return filter(features, feature_id)
    '''

@route('/api/layers/<layer_id>/joined/<joined_resources>/')
def joined_resources(joined_resources):
    ''' Returns a Collection+JSON containing all generic joined resources
        Resources discovery happens through layer_url.
        Can take query containing feature_url and additional params.

        Pseudocode:
        -----------
        call layer_metadata(layer_id):
        if has query params:
            return joined_resources_query(joined_resources, query)
        else:
            if layer has link to joined resource:
                GET joined_resource_url
                substitute hrefs
                return CJ
    '''

def joined_resources_query(joined_resources, query):
    ''' Returns a Collection+JSON containing generic joined resources.
        Resources have been filtered according to the query.
        Query may include original (db_api) feature_uri as parameter

        Pseudocode:
        -----------
        call layer_metadata(layer_id)
        if has query link matching query:
            GET joined_resource_url query
            subsittue hrefs
            return CJ
    '''
@route('/api/layers/<layer_id>/joined/<joined_resources>/<path:resource_url>')
def joined_resource(resource_id):
    ''' Returns a Collection+JSON containing the objects of the sub path.

        Pseudocode:
        -----------
        call layer_metadata
        if has joined_resource_uri:
            GET joined_resoure_uri resource_id
            subsitute hrefs
            return resource
    '''

@route('/api/layers/<layer_id>/joined/<joined_resources>/<resource_id>/<subresources_link>')
def joined_resource(resource_id):
    ''' Returns a Collection+JSON containing subresources of a joined resource.

        Pseudocode:
        -----------
        call layer_metadata
        if has joined_resource_uri:
            GET joined_resoure_uri resource_id
            subsitute hrefs
            return resource
