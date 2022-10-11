from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client

def get_index(index_name = 'cfe_product_Product'):
    client = get_client()
    index = client.init_index('cfe_product_Product')
    return index



def perform_seacrh(query,**kwargs):
    """
    perform_seacrh("hello", tags=["electronics"], public=True)
    """
    index = get_index()
    params = {}
    tags = ""
    if "tags":
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params['tagFilters'] = tags
    index_filters = [f"{k}:{v}" for k,v in kwargs.items() if v]
    if len(index_filters) != 0:
        params['faceFilters'] = index_filters
    results = index.search(query)
    return results
