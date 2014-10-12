LAYERS = ['http://localhost:5001', 'http://localhost:5002']

@route('/')
def redirect_to_layers():

@route('/api/layers/')
def list_layers():
    ''' Returns a Collection+JSON containing layer items

        Pseudocode:
        -----------
        for layer_server in LAYERS:
            GET  layer_server/
            RE layers collection
                nightlife/
                transport/

            substitue paths in hrefs

        append version
        append self href

        return CJ
    '''

@route('api/layers/<layer_id>')
def layer_metadata(layer_id):
    ''' Returns a Collection+JSON containing layer meta data.

        Pseudocode:
        -----------
        layers_collection = GET list_layers()
        match layer_id in layers_collection
        GET layer_collection from layer_url

        substitue paths in hrefs

        return CJ
    '''
