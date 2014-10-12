JOINS = 'http://localhost:6001'
NAME = 'nightlife'

app.route('/')
def layer():
    ''' Returns Collection+JSON with a single layer in it.
        A layer consists of:
            data:
                name
                description

            links:
                href self
                subresource profile:map features
                subresource profile:join RESOURCE
                icon ext:image
                profile ext:schema

            queries:
                templates exposed by join:
                    features/feature_id/RESOURCE?
                    joines/RESOURCE?
    '''
app.route('/features/')
def features():
    ''' Returns a Collection+JSON containing all features in this layer.
        A feature is a geographical mark on a map.
        Carries a geojson feature as a data propery.

        A feature item consists of:
            data:
                # name
                # description
                # geojson_feature
                # adress_string

            links:
                href self
                $ subresource RESOURCE
                # icon ext:img
                # profile ext:schema

        queries:
            template exposed by join:
            $    features/feature_id/RESOURCE?

        Note: fields with # come from db_resource, $ from join

    '''

app.route('/features/<feature_id>')
def feature('/features'):
    ''' Returns a Collection+JSON with the single feature matching feature_id.

        Simply calls features() and filters.
    '''


app.route('joins/')
def request_joins():
    ''' Returns a Collection+JSON with join items.
        join items are created in the joins resource.

        The items are expected to carry at least:
            data:
                name
                description
            links:
                href self
                subresource features
                subresource joined_resource_id
                profile ext:schema

        queries:
                exposed by joins service

        Pseudocode:
        ----------
        look up join__url in JOIN
        joins = GET join_url
        return joins
    '''
app.route('/features/<feature_id>/<joined_resource_id>')
def feature_join():
    ''' Returns Collection+JSON with generic joined resources.
        Should be used with a query.

        Pseudocode:
        calls request_joins()
        compare joined_resource_id with join name
        if not return error
        else
            resource = GET join_url/joined_resource_id?query+feature_url
        do not substitute href of resources!
        return resource
    '''

@app.route('joins/<joined_resource_id>')
def join(joined_resource_id):
    ''' Returns a Collection+JSON of feature items.
        The feature items where manipulated by the joins service.
        They now contain a link directly to the resource_url.
        Should be used with a query.
        Acts as filter of features based on whether a resource matches a query.

        Pseudocode:
        -----------
        call request_joins()
        compare joined_resource_id with join names
        if not found return error
        else
            features = GET join_url/joined_resource_id/features/query+features_url
            substiture hrefs to take ownership of features again
            return features
