JOINS = 'http://localhost:6001'
NAME = 'nightlife'


def get_joins():
    ''' GET join_url
        return response
    '''

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
                    features/q=RESOURCE?

        Pseudocode:
        -----------
        GET meta data fields from DB_url
        GET joins metadata (links, queries) via get_joins()
        compile into Collection+JSON
    '''
app.route('/features/')
def features():
    ''' Returns a Collection+JSON containing all features in this layer.
        A feature is a geographical mark on a map.
        Carries a geojson feature as a data propery.
        May be combined with a query that referes to a joined subresource

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

        Pseudocode:
        -----------
        if has query param `join`:
            return features_joined(query)

        else:
            GET join metadata (links, queries) via get_join()
            GET features from DB_url
            for each feature in features:
                compile queries/links from join metadata
                compile into Collection+JSON
            return CJ


    '''

def features_joined(query):
    ''' Returns a Collection+JSON containing feature items.
        In contrast to features() this function matches and validates a query
        against the availiable joins and then executes that query.
        It expects to receive features from the join service wich now carry a
        link to the query on the joined resource. If the query on the subresource
        returned no results the feature is filtered.

        Example:
        query = 'join=events&after=2014-1-1&before=2014-1-2'
        Feature contains link to/events?after=2014-1-1&before=2014-1-2' if
        it has events in the stated timeframe.

        Pseudocode:
        -----------
        unpack query parametes
        GET joins metadata (links, queries) via get_join
        test if `join` parameter matches name of a join
        test if other parameters match any of the queries on the relevant join
        if not return error
        else:
            request features from join by passing query, url to features
            and a KEY to use for joining.
            GET joins_url/join_name/?q=Query&features=features_url&key=Some_field
            substitute hrefs to claim ownership

    '''




app.route('/features/<feature_id>')
def feature('/features'):
    ''' Returns a Collection+JSON with the single feature matching feature_id.

        Simply calls features() and filters.
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
