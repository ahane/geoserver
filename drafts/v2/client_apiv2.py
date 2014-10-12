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
